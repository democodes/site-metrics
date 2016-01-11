import json
from pprint import pprint

with open('result.json') as data_file:    
    data = json.load(data_file)

#pprint(data)
print data["http://facebook.com"][0]
