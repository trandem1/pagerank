
import json

data = set()
from pyvi import ViTokenizer

def add_data(path):
    with open(path,"r") as lines:
        for line in lines:
            data.add(line)

# add_data("data/rawdata/dien_lanh")
# add_data("data/rawdata/dien_tu")
# add_data("data/rawdata/toy")
#
# fileWrite = open("finalData","w")
# for line in data:
#     fileWrite.write(line)
# fileWrite.close()

with open("finalData") as lines:
    fileWrite = open("datafinalToken","w")
    for line in lines:
        try:
            x = json.loads(line)
            cmt = ViTokenizer.tokenize(x['comment'].lower())
            fileWrite.write(str(x['star'])+"\t"+str(cmt))
            fileWrite.write("\n")
        except:
            print(line)

    fileWrite.close()