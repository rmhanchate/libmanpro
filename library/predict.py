# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
import joblib

data = pd.read_csv("data/books.csv",encoding = "ISO-8859-1")
columns = ['Id', 'Image', 'Image_link', 'Title', 'Author', 'Class', 'Genre']
data.columns = columns
books = pd.DataFrame(data['Title'])
author = pd.DataFrame(data['Author'])
genre = pd.DataFrame(data['Genre'])
data['Author'] = data['Author'].fillna('No Book')
data['Title'] = data['Title'].fillna('No Book')
data['everything'] = pd.DataFrame(data['Title'] + ' ' + data['Author'])
feat = ['Genre']
for x in feat:
    le = LabelEncoder()
    le.fit(list(genre[x].values))
    genre[x] = le.transform(list(genre[x]))
vectorizer = TfidfVectorizer(min_df=2, max_features=70000, strip_accents='unicode',
                             lowercase =True, analyzer='word', token_pattern=r'\w+', 
                             use_idf=True, smooth_idf=True, sublinear_tf=True, 
                             stop_words = 'english')
vectors = vectorizer.fit_transform(data['everything'])

def NaivBay(text):
    clf = joblib.load('models/gaussian.pkl')
    print(text)
    text = [text]
    text[0] = text[0].lower()
    s = (vectorizer.transform(text))
    encoded = (clf.predict(s))
    predicted = le.inverse_transform(encoded)[0]
    return predicted 
    
def LogReg(text):
    clf = joblib.load('models/logistic.pkl')
    print(text)
    text = [text]
    text[0] = text[0].lower()
    s = (vectorizer.transform(text))
    encoded = (clf.predict(s))
    predicted = le.inverse_transform(encoded)[0]
    return predicted   
    
def MLPskl(text):
    clf = joblib.load('model/mlpskl.pkl')
    print(text)
    text = [text]
    text[0] = text[0].lower()
    s = (vectorizer.transform(text))
    encoded = (clf.predict(s))
    predicted = le.inverse_transform(encoded)[0]
    return predicted 