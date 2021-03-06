import pandas as pd
import numpy as np
import sys
rootFileDirectory = "/home/ec2-user/FrequencyBounds/"
sys.path.append(rootFileDirectory + 'Source/ExperimentUtils')
from InferenceUtils import *

if __name__ == '__main__':
    
    benchmarks = ['JOBLight', 'JOBLightRanges', 'JOBM', 'Stats']

    methods = ['SafeBound', "Postgres", "Postgres2D", "BayesCard", "PessemisticCardinality"]

    PostgresParams = [10, 100, 1000, 5000, 10000]

    Postgres2DParams = [10, 100, 1000, 5000, 10000]
    
    '''
    for i in range(1,6):
        for benchmark in benchmarks:
            statsFile = rootFileDirectory + "StatObjects/SafeBound_" + str(i)  + "_" + benchmark + ".pkl"
            outputFile = rootFileDirectory + "Data/Results/SafeBound_Inference_" + str(i) + "_" + benchmark + ".csv"
            evaluate_inference(method = 'SafeBound', 
                               statsFile =  statsFile,
                               benchmark = benchmark,
                               outputFile = outputFile,
                               statisticsTarget = None)
    for i in range(1,6):
        for benchmark in benchmarks:
            outputFile = rootFileDirectory + "Data/Results/Postgres_Inference_" + str(i) + "_" + benchmark  + ".csv"
            evaluate_inference(method = 'Postgres', 
                               statsFile =  None,
                               benchmark = benchmark,
                               outputFile = outputFile,
                               statisticsTarget = PostgresParams[i-1])

    for i in range(1,6):
        for benchmark in benchmarks:
            outputFile = rootFileDirectory + "Data/Results/Postgres2D_Inference_" + str(i) + "_"  + benchmark + ".csv"
            evaluate_inference(method = 'Postgres2D', 
                               statsFile =  None,
                               benchmark = benchmark,
                               outputFile = outputFile,
                               statisticsTarget = Postgres2DParams[i-1])
    
     
    for benchmark in benchmarks:
        outputFile = rootFileDirectory + "Data/Results/BayesCard_Inference_"  + benchmark + ".csv"
        ensembleDirectory = rootFileDirectory + "StatObjects/BayesCardEnsembles/" + benchmark +"/"
        evaluate_inference(method = 'BayesCard', 
                           statsFile =  ensembleDirectory,
                           benchmark = benchmark,
                           outputFile = outputFile)
        
    
    for benchmark in benchmarks:
        outputFile = rootFileDirectory + "Data/Results/PessemisticCardinality_Inference_"  + benchmark + ".csv"
        ensembleDirectory = rootFileDirectory + "StatObjects/BayesCardEnsembles/" + benchmark +"/"
        evaluate_inference(method = 'PessemisticCardinality', 
                           statsFile =  ensembleDirectory,
                           benchmark = benchmark,
                           outputFile = outputFile)
    ''' 
