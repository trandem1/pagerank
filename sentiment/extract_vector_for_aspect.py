from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import json
from pyvi import ViTokenizer
import pickle
import os

def read_data_from_folder(folder_path):
    X =[]
    y =[]
    for filename in os.listdir(folder_path):
        with open(folder_path+"/"+filename) as lines:
            for line in lines:
                try:
                    json_data = json.loads(line)
                    X.append(ViTokenizer.tokenize(json_data['comment']))
                    # y.append(filename)
                    if(filename == "dien_lanh"):
                        y.append(0)
                    elif(filename =="comment1"):
                        y.append(1)
                    else:
                        y.append(2)
                except:
                    print(line)
    return X,y

def fit_tranfrom_and_save_ngam_from_data(n,data):
    ngram = CountVectorizer(ngram_range=(n,n))
    ngram.fit(data)
    pickle.dump(ngram,open("model/ngram","wb"))
    return ngram.transform(data)

def fit_tranfrom_and_save_tfidf_from_data(data):
    tfidf_transformer = TfidfTransformer()
    tfidf_transformer.fit(data)
    pickle.dump(tfidf_transformer,open("model/tfidf","wb"))
    return tfidf_transformer.transform(data)

def parse_data_to_idf_vector(data):
    ngram = pickle.load(open("model/ngram","rb"))
    idf = pickle.load(open("model/tfidf","rb"))
    data_tranfrom = idf.transform(ngram.transform(data))
    return data_tranfrom

