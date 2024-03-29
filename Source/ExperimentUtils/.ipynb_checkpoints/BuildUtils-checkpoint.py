import pandas as pd
import pickle
from datetime import datetime, timedelta
import os
import sys
rootFileDirectory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) +'/'
sys.path.append(rootFileDirectory + 'Source')
sys.path.append(rootFileDirectory + 'Source/ExperimentUtils')
from SafeBoundUtils import *
from DBConnectionUtils import *
from LoadUtils import *
sys.path.append(rootFileDirectory + 'bayescard')
from Schemas.stats.schema import gen_stats_light_schema
from Schemas.imdb.schema import gen_job_light_imdb_schema
from DataPrepare.join_data_preparation import JoinDataPreparator
from Models.Bayescard_BN import Bayescard_BN, build_meta_info
from DeepDBUtils.evaluation.utils import timestamp_transorform

def build_safe_bound(benchmark, parameters, outputFile):
    tableDFs = None
    tableNames = None
    joinColumns = None
    filterColumns = None
    FKtoKDict = None
    relativeErrorPerSegment = parameters['relativeErrorPerSegment']
    numHistogramBuckets = parameters['numHistogramBuckets']
    numEqualityOutliers = parameters['numEqualityOutliers']
    numCDFGroups = parameters['numCDFGroups']
    trackNulls = parameters['trackNulls']
    trackBiGrams = parameters['trackBiGrams']
    numCores = parameters['numCores']
    verbose = parameters['verbose']
    groupingMethod = parameters["groupingMethod"]
    modelCDF = parameters["modelCDF"]
    
    
    if benchmark == 'JOBLight':
        data = load_imdb()
        
        tableNames = ["cast_info", 
                      "movie_companies",
                      "movie_info_idx",
                      "movie_info",
                      "movie_keyword",
                      "title"]

        joinColumns = [["movie_id"],
                             ["movie_id"],
                             ["movie_id"],
                             ["movie_id"],
                             ["movie_id"],
                             ["id", "kind_id"]
                            ]
        
        filterColumns = [["role_id", "nr_order"],
                               ["company_type_id", 'company_id'],
                               ["info_type_id"],
                               ["info_type_id"],
                               ["keyword_id"],
                               ["episode_nr", "season_nr", "production_year", "kind_id"]
                              ]
        
        tableDFs = [data[table][list(set(joinColumns[i] + filterColumns[i]))] for i, table in enumerate(tableNames)]
        del data
        
        FKtoKDict = {"cast_info":[["movie_id", "id", "title"]],
                    "movie_companies":[["movie_id", "id", "title"]],
                    "movie_info":[["movie_id", "id", "title"]],
                    "movie_info_idx":[["movie_id", "id", "title"]],
                    "movie_keyword":[["movie_id", "id", "title"]]
                    }
        
    elif benchmark == 'JOBLightRanges':
        data = load_imdb()    

        tableNames = ["cast_info", "movie_companies", "movie_info_idx", "movie_info",
                     "movie_keyword", "title"]
                  
        joinColumns = [ ["movie_id"],
                        ["movie_id"],
                        ["movie_id"],
                        ["movie_id"],
                        ["movie_id"],
                        ["id", "kind_id"]
                        ]
        filterColumns = [
                        ["role_id", "nr_order"],
                        ["company_type_id", 'company_id'],
                        ["info_type_id"],
                        ["info_type_id"],
                        ["keyword_id"],
                        ["episode_nr", "season_nr", "production_year", "series_years", "kind_id", 'phonetic_code', 'series_years', 'imdb_index']
                        ]
        tableDFs = [data[table][list(set(joinColumns[i] + filterColumns[i]))] for i, table in enumerate(tableNames)]
        del data
        
        FKtoKDict = {"cast_info":[["movie_id", "id", "title"]],
                    "movie_companies":[["movie_id", "id", "title"]],
                    "movie_info":[["movie_id", "id", "title"]],
                    "movie_info_idx":[["movie_id", "id", "title"]],
                    "movie_keyword":[["movie_id", "id", "title"]]
                    }
        
    elif benchmark == 'JOBM': 
        data = load_imdb()

        tableNames = [ "cast_info", "aka_name", "aka_title",
                          "comp_cast_type", "company_name",
                     "company_type", "complete_cast", "info_type",
                     "keyword", "kind_type", "link_type",
                     "movie_companies", "movie_info_idx", "movie_info",
                     "movie_keyword", "movie_link", "role_type", "title"]
        
        joinColumns = [
                           ["id", "person_id", "movie_id", "person_role_id", "role_id"],
                           ["id", "person_id"],
                           ["id", "movie_id", "kind_id"],
                           ["id"],
                           ["id"],
                           ["id"],
                           ["id", "movie_id", "subject_id", "status_id"],
                           ["id"],
                           ["id"],
                           ["id"],
                           ["id"],
                           ["id", "movie_id", "company_id", "company_type_id"],
                           ["id", "movie_id", "info_type_id"],
                           ["id", "movie_id", "info_type_id"],
                           ["id", "movie_id", "keyword_id"],
                           ["id", "movie_id", "linked_movie_id", "link_type_id"],
                           ["id"],
                           ["id", "kind_id"]
                          ]

        filterColumns = [["note"],
                           [],
                           [],
                           ["kind"],
                           ["country_code", "name"],
                           ["kind"],
                           [],
                           ["info"],
                           ["keyword"],
                           ["kind"],
                           ["link"],
                           ["note"],
                           ["info"],
                           ["info", "note"],
                           [],
                           [],
                           [],
                           ["episode_nr", "production_year", "title"]
                        ]
                
        tableDFs = [data[table][list(set(joinColumns[i] + filterColumns[i]))] for i, table in enumerate(tableNames)]
        del data
        
        FKtoKDict = {"aka_title":[["movie_id", "id", "title"], ["kind_id", "id", "kind_type"]],
                     "cast_info":[["movie_id", "id", "title"],
                                  ["person_role_id", "id", "char_name"],
                                  ["role_id", "id", "role_type"]],
                    "movie_companies":[["movie_id", "id", "title"],
                                      ["company_id", "id", "company_name"],
                                      ["company_type_id", "id", "company_type"]],
                    "movie_info":[["movie_id", "id", "title"],
                                 ["info_type_id", "id", "info_type"]],
                    "movie_info_idx":[["movie_id", "id", "title"],
                                     ["info_type_id", "id", "info_type"]],
                    "movie_keyword":[["movie_id", "id", "title"],
                                    ["keyword_id", "id", "keyword"]],
                    "person_info":[["info_type_id", "id", "info_type"]],
                    }
        
    elif benchmark == 'Stats':
        data = load_stats()
        
        tableNames = ["badges",
                      "comments", 
                      "postHistory",
                      "postLinks", 
                      "posts", 
                      "tags", 
                      "users", 
                      "votes"]
        
        joinColumns = [["Id","UserId"], 
                        ["Id", "PostId", "UserId"],
                        ["Id", "PostId", "UserId"],
                        ["Id", "PostId", "RelatedPostId"],
                        ["Id", "OwnerUserId", "LastEditorUserId"],
                        ["Id", "ExcerptPostId"],
                        ["Id"],
                        ["Id", "PostId", "UserId"]]
        filterColumns = [["Date"],
                          ["Score", "CreationDate"],
                          ["PostHistoryTypeId", "CreationDate"],
                          ["CreationDate", "LinkTypeId"],
                          ["PostTypeId", "CreationDate", "Score", "ViewCount", "AnswerCount", "CommentCount", "FavoriteCount"],
                          ["Count"],
                          ["Reputation", "CreationDate", "Views", "UpVotes", "DownVotes"],
                          ["VoteTypeId", "CreationDate", "BountyAmount"]
                        ]
                
        tableDFs = [data[table][list(set(joinColumns[i] + filterColumns[i]))] for i, table in enumerate(tableNames)]
        del data
        
        FKtoKDict = {"badges":[["UserId", "Id", "users"]],
                     "comments":[["PostId", "Id", "posts"], ["UserId", "Id", "users"]],
                     "postHistory":[["PostId", "Id", "posts"], ["UserId", "Id", "users"]],
                     "postLinks":[["PostId", "Id", "posts"]],
                     "posts":[["OwnerUserId", "Id", "users"]],
                     "tags":[["ExcerptPostId", "Id", "posts"]],
                     "votes":[["UserId", "Id", "users"],["PostId", "Id", "posts"]]
                    }
        
    buildStart = datetime.now()
    stats = SafeBound(tableDFs= tableDFs,
                      tableNames=tableNames,
                      tableJoinCols = joinColumns,
                      originalFilterCols = filterColumns,
                      relativeErrorPerSegment = relativeErrorPerSegment,
                      numHistogramBuckets = numHistogramBuckets, 
                      numEqualityOutliers= numEqualityOutliers,
                      FKtoKDict=FKtoKDict,
                      numCDFGroups = numCDFGroups,
                      trackNulls = trackNulls,
                      trackBiGrams=trackBiGrams,
                      numCores=numCores,
                      groupingMethod=groupingMethod,
                      modelCDF=modelCDF,
                      verbose=verbose)
    buildEnd = datetime.now()
    buildSeconds = (buildEnd-buildStart).total_seconds()
    pickle.dump(stats, open(outputFile, "wb" ))
    return buildSeconds, stats.memory()

def build_postgres(benchmark, parameters):
    
    statisticsTarget = parameters['statisticsTarget']
    dbConn = None
    if benchmark == 'JOBLight':
        dbConn = getDBConn('imdblight')
    elif benchmark == 'JOBLightRanges':
        dbConn = getDBConn('imdblightranges')
    elif benchmark == 'JOBM':
        dbConn = getDBConn('imdbm')
    elif benchmark == 'Stats':
        dbConn = getDBConn('stats')
    elif benchmark == 'JOBLight2D':
        dbConn = getDBConn('imdblight2d')
    elif benchmark == 'JOBLightRanges2D':
        dbConn = getDBConn('imdblightranges2d')
    elif benchmark == 'JOBM2D':
        dbConn = getDBConn('imdbm2d')
    elif benchmark == 'Stats2D':
        dbConn = getDBConn('stats2d')
    
    dbConn.changeStatisticsTarget(statisticsTarget)
    buildStart = datetime.now()
    dbConn.runAnalyze()
    buildEnd = datetime.now()
    return (buildEnd-buildStart).total_seconds(), dbConn.memory()

def build_bayes_card(benchmark, parameters, outputFolder):
    
    hdfPath = None
    csvPath = None
    schema = None
    
    if benchmark == 'Stats':
        hdfPath = rootDirectory + "Data/Stats/stats_simplified_bayes_card/stats_hdf"
        csvPath = rootDirectory + "Data/Stats/stats_simplified_bayes_card"
        schema = gen_stats_light_schema(csvPath)
    elif benchmark == 'JOBLight':
        hdfPath = rootDirectory + "Data/JOB/JOB_hdf"
        csvPath = rootDirectory + "Data/JOB"
        schema = gen_job_light_imdb_schema(csvPath)
    else:
        return 0,0
        
    buildStart = datetime.now()
    metaDataPath = hdfPath + '/meta_data.pkl'
    prep = JoinDataPreparator(metaDataPath, schema, max_table_data=20000000)
    
    algorithm = "chow-liu"
    maxParents = 1
    sampleSize = 200000
    modelSize = 0
    for i, relationship_obj in enumerate(schema.relationships):
        dfSampleSize = 10000000
        relation = [relationship_obj.identifier]
        df, metaTypes, nullValues, fullJoinEst = prep.generate_n_samples(dfSampleSize,
                                                                        relationship_list=relation,
                                                                        post_sampling_factor=10)
        columns = list(df.columns)
        assert len(columns) == len(metaTypes) == len(nullValues)
        metaInfo = build_meta_info(df.columns, nullValues)
        bn = Bayescard_BN(schema, relation, column_names=columns, full_join_size=len(df),
                          table_meta_data=prep.table_meta_data, meta_types=metaTypes, null_values=nullValues,
                          meta_info=metaInfo)
        modelPath = outputFolder + f"/{i}_{algorithm}_{maxParents}.pkl"
        bn.build_from_data(df, algorithm=algorithm, max_parents=maxParents, ignore_cols=['Id'],
                           sample_size=sampleSize)
        pickle.dump(bn, open(modelPath, 'wb'), pickle.HIGHEST_PROTOCOL)
        modelSize +=  os.path.getsize(modelPath)
    buildEnd = datetime.now()
    return (buildEnd-buildStart).total_seconds(), modelSize

    
def build_stats_object(method = 'SafeBound',
                       benchmark = 'JOBLight',
                       parameters = dict(), 
                       outputFile = "../../StatObjects/SafeBound_JOBLight.pkl"):    

    if method == 'SafeBound':
        return build_safe_bound(benchmark, parameters, outputFile)
    
    elif method == 'Postgres':
        return build_postgres(benchmark, parameters)

    elif method == 'Postgres2D':
        return build_postgres(benchmark + "2D", parameters)
    
    elif method == 'BayesCard':
        return build_bayes_card(benchmark, parameters, outputFile)
    
    elif method == 'PessimisticCardinality':
        return -1
    
    else:
        return -1
    

    
    


