import json

with open("json/student.json", 'r') as f: # loading json from json file
    data = json.load(f)

# print(data)

with open("json/data2.json", 'w') as f:
    json.dump(data, f) # we need to refer to file to dump +_+