import json
import sys
  
fileName = sys.argv[1]

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y) 
with open(fileName, "w") as outfile:
    outfile.write(y)
 