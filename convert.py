import csv 
import json 
import collections
import pandas as pd
import kaggle

kaggle.api.authenticate()

kaggle.api.dataset_download_files('jrobischon/wikipedia-movie-plots', path="downloaded_file", unzip=True)

orderedDict = collections.OrderedDict()
from collections import OrderedDict
def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
    x = OrderedDict([('index', {})])      
    jsonString = json.dumps(x)  
    with open(csvFilePath, encoding='utf-8') as csvf: 
        with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
            csvReader = csv.DictReader(csvf) 
            for row in csvReader: 
                jsonf.write(jsonString)
                jsonf.write("\n")
                y = json.dumps(row)
                jsonf.write(y)
                jsonf.write("\n")
          
csvFilePath = r'/home/sanskar/github/elasticsearch-is-going-to-be-the-end-of-me/downloaded_file/wiki_movie_plots_deduped.csv'
jsonFilePath = r'/home/sanskar/github/elasticsearch-is-going-to-be-the-end-of-me/naveen.json'

df = pd.read_csv(csvFilePath)

df2 = df[:1000]

df2.to_csv(csvFilePath, index = False)

csv_to_json(csvFilePath, jsonFilePath)