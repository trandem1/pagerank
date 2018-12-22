import sentiment.extract_vector_for_aspect as preprocess
import pickle
from sklearn import svm
from sklearn.pipeline import Pipeline

def train_data():
    folderpath = "/home/trandem/PycharmProjects/pageRank/sentiment/data/rawdata"
    X, y = preprocess.read_data_from_folder(folderpath)
    ngram = pickle.load(open("model/ngram", "rb"))
    tfidf = pickle.load(open("model/tfidf", "rb"))
    X = tfidf.transform(ngram.transform(X))
    clf = svm.SVC(gamma='scale', decision_function_shape='ovo')
    clf.fit(X, y)
    text_clf = Pipeline([
        ('vect', ngram),
        ('tfidf', tfidf),
        ('clf', clf),
    ])
    pickle.dump(clf, open("model/aspect", "wb"))
    pickle.dump(text_clf, open("model/pipeline_aspect", "wb"))

def get_aspect_data(data):
    text_clf = pickle.load(open("model/pipeline_aspect","rb"))
    return text_clf.predict(data)
