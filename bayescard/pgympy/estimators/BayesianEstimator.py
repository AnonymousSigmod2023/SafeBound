# -*- coding: utf-8 -*-

from itertools import chain

import numpy as np
import numbers

from Pgmpy.estimators import ParameterEstimator
from Pgmpy.factors.discrete import TabularCPD
from Pgmpy.models import BayesianModel


class BayesianEstimator(ParameterEstimator):
    def __init__(self, model, data, **kwargs):
        """
        Class used to compute parameters for a model using Bayesian Parameter Estimation.
        See `MaximumLikelihoodEstimator` for constructor parameters.
        """
        if not isinstance(model, BayesianModel):
            raise NotImplementedError(
                "Bayesian Parameter Estimation is only implemented for BayesianModel"
            )

        super(BayesianEstimator, self).__init__(model, data, **kwargs)

    def get_parameters(
        self, prior_type="BDeu", equivalent_sample_size=5, pseudo_counts=None
    ):
        """
        Method to estimate the model parameters (CPDs).

        Parameters
        ----------
        prior_type: 'dirichlet', 'BDeu', or 'K2'
            string indicting which type of prior to use for the model parameters.
            - If 'prior_type' is 'dirichlet', the following must be provided:
                'pseudo_counts' = dirichlet hyperparameters; a single number or a dict containing, for each
                 variable, a 2-D array of the shape (node_card, product of parents_card) with a "virtual"
                 count for each variable state in the CPD, that is added to the state counts.
                 (lexicographic ordering of states assumed)
            - If 'prior_type' is 'BDeu', then an 'equivalent_sample_size'
                must be specified instead of 'pseudo_counts'. This is equivalent to
                'prior_type=dirichlet' and using uniform 'pseudo_counts' of
                `equivalent_sample_size/(node_cardinality*np.prod(parents_cardinalities))` for each node.
                'equivalent_sample_size' can either be a numerical value or a dict that specifies
                the size for each variable separately.
            - A prior_type of 'K2' is a shorthand for 'dirichlet' + setting every pseudo_count to 1,
                regardless of the cardinality of the variable.

        Returns
        -------
        parameters: list
            List of TabularCPDs, one for each variable of the model
        """
        parameters = []
        for node in self.model.nodes():
            _equivalent_sample_size = (
                equivalent_sample_size[node]
                if isinstance(equivalent_sample_size, dict)
                else equivalent_sample_size
            )
            if isinstance(pseudo_counts, numbers.Real):
                _pseudo_counts = pseudo_counts
            else:
                _pseudo_counts = pseudo_counts[node] if pseudo_counts else None

            cpd = self.estimate_cpd(
                node,
                prior_type=prior_type,
                equivalent_sample_size=_equivalent_sample_size,
                pseudo_counts=_pseudo_counts,
            )
            parameters.append(cpd)

        return parameters

    def estimate_cpd(
        self, node, prior_type="BDeu", pseudo_counts=[], equivalent_sample_size=5
    ):
        """
        Method to estimate the CPD for a given variable.

        Parameters
        ----------
        node: int, string (any hashable python object)
            The name of the variable for which the CPD is to be estimated.

        prior_type: 'dirichlet', 'BDeu', 'K2',
            string indicting which type of prior to use for the model parameters.
            - If 'prior_type' is 'dirichlet', the following must be provided:
                'pseudo_counts' = dirichlet hyperparameters; a single number or 2-D array of shape
                 (node_card, product of parents_card) with a "virtual" count for
                 each variable state in the CPD.
                 The virtual counts are added to the actual state counts found in the data.
                 (if a list is provided, a lexicographic ordering of states is assumed)
            - If 'prior_type' is 'BDeu', then an 'equivalent_sample_size'
                must be specified instead of 'pseudo_counts'. This is equivalent to
                'prior_type=dirichlet' and using uniform 'pseudo_counts' of
                `equivalent_sample_size/(node_cardinality*np.prod(parents_cardinalities))`.
            - A prior_type of 'K2' is a shorthand for 'dirichlet' + setting every pseudo_count to 1,
                regardless of the cardinality of the variable.

        Returns
        -------
        CPD: TabularCPD
        """
        node_cardinality = len(self.state_names[node])
        parents = sorted(self.model.get_parents(node))
        parents_cardinalities = [len(self.state_names[parent]) for parent in parents]
        cpd_shape = (node_cardinality, np.prod(parents_cardinalities, dtype=int))

        if prior_type == "K2":
            pseudo_counts = np.ones(cpd_shape, dtype=int)
        elif prior_type == "BDeu":
            alpha = float(equivalent_sample_size) / (
                node_cardinality * np.prod(parents_cardinalities)
            )
            pseudo_counts = np.ones(cpd_shape, dtype=float) * alpha
        elif prior_type == "dirichlet":
            if isinstance(pseudo_counts, numbers.Real):
                pseudo_counts = np.ones(cpd_shape, dtype=int) * pseudo_counts

            else:
                pseudo_counts = np.array(pseudo_counts)
                if pseudo_counts.shape != cpd_shape:
                    raise ValueError(
                        "The shape of pseudo_counts for the node: {node} must be of shape: {shape}".format(
                            node=node, shape=str(cpd_shape)
                        )
                    )
        else:
            raise ValueError("'prior_type' not specified")

        state_counts = self.state_counts(node)
        bayesian_counts = state_counts + pseudo_counts

        cpd = TabularCPD(
            node,
            node_cardinality,
            np.array(bayesian_counts),
            evidence=parents,
            evidence_card=parents_cardinalities,
            state_names={var: self.state_names[var] for var in chain([node], parents)},
        )
        cpd.normalize()
        return cpd
