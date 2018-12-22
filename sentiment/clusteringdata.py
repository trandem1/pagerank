
import sentiment.extractVector_for_sentiment as extract
import pickle
import json

from pyvi import ViTokenizer

as_pect_dist =dict()

as_pect_dist [0] = "Chất lượng sản phẩm"
as_pect_dist [1]= "Chất lượng dịch vụ"
as_pect_dist [2]= "Chất lượng sản phẩm"
as_pect_dist [3]= "Chất lượng dịch vụ"
as_pect_dist [4]= "Chất lượng dịch vụ"
as_pect_dist [5]= "Chất lượng sản phẩm"
as_pect_dist [6]= "Chất lượng sản phẩm"
as_pect_dist [7]= "Chất lượng dịch vụ"
as_pect_dist [8]= "Chất lượng dịch vụ"
as_pect_dist [9]= "Giá thành"



def find_max_value_index(list):
    index = 0
    value =0
    for i in range(len(list)):
        if (list[i]) >value:
            value = list[i]
            index =i
    return index

lda = pickle.load(open("model/lda", "rb"))
# while(True):
#     test = input("enter the test \n")
#
#     X = extract.parse_data_to_idf_vector([test])
#
#     tran = lda.transform(X)[0]
#     print(tran)
#
#     index = find_max_value_index(tran)
#     print(as_pect_dist[index])

as_pect =dict()
as_pect["Chất lượng sản phẩm"] = 1
as_pect["Chất lượng dịch vụ"] =2
as_pect["Giá thành"] = 3

X=[]
Y=[]
def read_data_from_file(file_name):
    dem =1
    with open(file_name) as lines:
        for line in lines :
            try:
                x = json.loads(line)
                X.append((x['comment']))
                Y.append(x['espected'])
                dem = dem+1
                if dem >500: break
            except :
                print("lol"+line)

y_predict =[]

def predict(list):
    lda = pickle.load(open("model/lda", "rb"))
    data = extract.parse_data_to_idf_vector(list)
    trans = lda.transform(data)
    for dt in trans:
        # print(as_pect_dist[find_max_value_index(dt)])
        test = as_pect[as_pect_dist[find_max_value_index(dt)]]
        y_predict.append(test)

read_data_from_file("dien_lanh")
predict(X)
from sklearn.metrics import classification_report

print(classification_report(Y, y_predict,target_names=["Chất lượng sản phẩm","Chất lượng dịch vụ","Giá thành"]))