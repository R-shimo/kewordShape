import pickle
import re

inputName = "input.txt"
outputName = "myhorselist.pkl"
data = []
elem = {}

with open("%s"%inputName, 'r') as i:
  textLine = i.readlines()
  for text in textLine:
    elem["name"] = text.rstrip('\n').decode('utf-8')
    data.append(elem.copy())


with open("%s"%outputName, 'wb') as o:
  pickle.dump(data, o)
