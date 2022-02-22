import json

# ---------------------------------------------
# import package to read json
# ---------------------------------------------


# ---------------------------------------------
#  write function to load file and parse json
# ---------------------------------------------

def readJson(file):
    with open(file) as p:
        return json.load(p)

# ---------------------------------------------
#  call 'readJson', load salaries
# ---------------------------------------------

salaries = readJson('./data.json')
# print(salaries)

# ---------------------------------------------
#  print all salaries
# ---------------------------------------------

for salary in salaries['data']:
    print(float(salary[18]))

# ---------------------------------------------
# loop through list, only print salary field
# ---------------------------------------------


# ---------------------------------------------
#  add all salaries
# ---------------------------------------------