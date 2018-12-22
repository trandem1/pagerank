from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from pyvi import ViTokenizer

import json

X =[]
Y = []
stop_word =[]
#doc data 1,2 sao


def read_data_from_file(file_name):
    with open(file_name) as lines:
        tieucuc = 0
        tichcuc = 0
        for line in lines :
            try:
                x = json.loads(line)
                if x['star'] == 3:
                    continue

                if x['star']== 1 or x['star'] == 2:
                    if(tieucuc<500):
                        X.append(ViTokenizer.tokenize(x['comment']))
                        Y.append(1)
                    tieucuc = tieucuc +1
                # if x['star'] == '3.0':
                #     Y.append(2)
                if x['star'] == 4 or x['star'] == 5 :
                    if(tichcuc <500):
                        X.append(ViTokenizer.tokenize(x['comment']))
                        Y.append(2)
                    tichcuc = tichcuc + 1
            except :
                print("lol"+line)

def read_stop_word(stopfile):
    with open(stopfile) as lines:
        for line in lines:
            stop_word.append(line)

read_stop_word("stop_word.txt")
read_data_from_file("finalData")
print(len(X))

bigram_vectorizer = CountVectorizer(ngram_range=(2,2),stop_words=stop_word)

X_train_counts = bigram_vectorizer.fit_transform(X)

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)



from sklearn import svm

X_train_tranfom  = tfidf_transformer.transform(bigram_vectorizer.transform(X_train))
X_test_tranfom = tfidf_transformer.transform(bigram_vectorizer.transform(X_test))

clf = svm.SVC(gamma='scale',kernel='linear')
clf.fit(X_train_tranfom,y_train)

from sklearn.metrics import classification_report

y_predict = clf.predict(X_test_tranfom)
print(classification_report(y_test, y_predict,target_names =["tieu cuc","tich cuc"]))


clf = svm.SVC(gamma='scale',kernel='poly')
clf.fit(X_train_tranfom,y_train)

y_predict = clf.predict(X_test_tranfom)
print(classification_report(y_test, y_predict,target_names =["tieu cuc","tich cuc"]))

clf = svm.SVC(gamma='scale',kernel='sigmoid')
clf.fit(X_train_tranfom,y_train)

from sklearn.metrics import classification_report

y_predict = clf.predict(X_test_tranfom)
print(classification_report(y_test, y_predict,target_names =["tieu cuc","tich cuc"]))

clf = svm.SVC(gamma='scale',kernel='rbf')
clf.fit(X_train_tranfom,y_train)

from sklearn.metrics import classification_report

y_predict = clf.predict(X_test_tranfom)
print(classification_report(y_test, y_predict,target_names =["tieu cuc","tich cuc"]))