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
                    star_num = int(json_data['star'])
                    y.append(get_sentiment_from_star(star_num))
                except:
                    print(line)
    return X,y

def get_sentiment_from_star(num_star):
    if(num_star == 5):
        sentiment ="tich_cuc"
    elif (num_star == 3 or num_star == 4):
        sentiment = "trung_binh"
    else:
        sentiment = "tieu_cuc"
    return sentiment

def read_data_from_file_to_list(file_name):
    X=[]
    y=[]
    with open(file_name) as lines:
        for line in lines:
            try:
                json_data = json.loads(line)
                X.append(ViTokenizer.tokenize(json_data['comment']))
                star_num = int(json_data['star'])
                y.append(get_sentiment_from_star(star_num))
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



