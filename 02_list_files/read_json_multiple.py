import json
import glob

# -------------------------------------
# import package to read json
# import package to walk file system
# -------------------------------------

pattern = './data/*/*.json'
data = []

for file in glob.glob(pattern):
    data.append(file)

# print(data)

# -----------------------------------
#  list all files
# -----------------------------------


# -----------------------------------
#  loop through files, parse json
# -----------------------------------

def readJson(file):
    with open(file) as p:
        return json.load(p)

filelist = []

for file in glob.glob(pattern):
    filelist.append(readJson(file))

print(filelist)