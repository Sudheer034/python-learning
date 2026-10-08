import json

# declaring a json string in python file
json_string = '''
{
  "student": [
  {
    "Name": "red",
    "id": 1
  },
  {
    "Name": "blue",
    "id": 2
   }]
}
'''

data = json.loads(json_string) # loads, 's' for string

data["Real"] = ["TRUE", "FALSE"] # creating a new column, after student

data2 = json.dumps(data) # dumps the data to data2

print(data2) # data is also same