from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

from pyvi import ViTokenizer, ViPosTagger



import json



X =[]
Y = []
#doc data 1,2 sao
def read_data_from_file(file_name):
    with open(file_name) as lines:
        for line in lines :
            try:
                x = json.loads(line)
                X.append(ViTokenizer.tokenize(x['comment']))
                Y.append(x['star'])
            except :
                print(line)

read_data_from_file("data/3sao")
read_data_from_file("data/1sao")
read_data_from_file("data/2sao")

#doc data 4,5 sao
def read_data_high():
    dem =0
    limit = 380
    with open("data/4sao") as lines:
        for line in lines:
            try:
                dem = dem +1
                if(dem < limit):
                    x = json.loads(line)
                    X.append(x['comment'])
                    Y.append(x['star'])
            except:
                print(line)
    dem =0
    with open("data/5sao") as lines:
        for line in lines:
            try:
                dem = dem +1
                if(dem < limit):
                    x = json.loads(line)
                    X.append(x['comment'])
                    Y.append(x['star'])
            except:
                print(line)
read_data_high()

bigram_vectorizer = CountVectorizer(ngram_range=(2,3))

X_train_counts = bigram_vectorizer.fit_transform(X)

print(bigram_vectorizer.vocabulary_.items())

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

X_train, X_test, y_train, y_test = train_test_split(X_train_tfidf, Y, test_size=0.33, random_state=42)

clf = MultinomialNB().fit(X_train, y_train)

from sklearn.metrics import classification_report

y_predict = clf.predict(X_test)
print(classification_report(y_test, y_predict,target_names =["tich cuc","tieu cuc", "trung binh"]))
