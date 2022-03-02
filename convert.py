import csv 
import json 
import collections
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
          
csvFilePath = r'/home/sanskar/test/wiki_movie_plots_deduped.csv'
jsonFilePath = r'/home/sanskar/test/newsmaplsldlfks.json'
csv_to_json(csvFilePath, jsonFilePath)