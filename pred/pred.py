# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 20:34:45 2020

@author: Rahul
"""

import re
import joblib
import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn import linear_model
from nltk.corpus import stopwords
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder
from sklearn.neural_network import MLPClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score

data = pd.read_csv("../data/books.csv",encoding = "ISO-8859-1")

columns = ['Id', 'Image', 'Image_link', 'Title', 'Author', 'Class', 'Genre']
data.columns = columns
books = pd.DataFrame(data['Title'])
author = pd.DataFrame(data['Author'])
genre = pd.DataFrame(data['Genre'])
data['Author'] = data['Author'].fillna('No Book')
data['Title'] = data['Title'].fillna('No Book')

feat = ['Genre']
for x in feat:
    le = LabelEncoder()
    le.fit(list(genre[x].values))
    genre[x] = le.transform(list(genre[x]))
data['everything'] = pd.DataFrame(data['Title'] + ' ' + data['Author'])

def change(t):
    t = t.split()
    return ' '.join([(i) for (i) in t if i not in stop])
stop = list(stopwords.words('english'))
data['everything'].apply(change)

vectorizer = TfidfVectorizer(min_df=2, max_features=70000, strip_accents='unicode',
                             lowercase =True, analyzer='word', token_pattern=r'\w+', 
                             use_idf=True, smooth_idf=True, sublinear_tf=True, 
                             stop_words = 'english')
vectors = vectorizer.fit_transform(data['everything'])

X_train, X_test, y_train, y_test = train_test_split(vectors, genre['Genre'], 
                                                    test_size=0.02)

clf = MultinomialNB(alpha=.45)
clf.fit(X_train, y_train)
pred = clf.predict(X_test)
print('Multinominal NaiveBayes: ')
print(metrics.accuracy_score(y_test, pred))
joblib.dump(clf, '../models/gaussian.pkl')
print("Model Saved")

clf = linear_model.LogisticRegression(solver= 'sag',max_iter=200,random_state=450)
clf.fit(X_train, y_train)
pred = clf.predict(X_test)
print('Logistic Regression: ')
print(metrics.accuracy_score(y_test, pred))
joblib.dump(clf, '../models/logistic.pkl')
print("Model Saved")

clf = MLPClassifier(activation='relu', alpha=0.00003, batch_size='auto',
                    beta_1=0.9, beta_2=0.999, early_stopping=False,
                    epsilon=1e-08, hidden_layer_sizes=(20,), learning_rate='constant',
                    learning_rate_init=0.003, max_iter=200, momentum=0.9,
                    nesterovs_momentum=True, power_t=0.5, random_state=1, shuffle=True,
                    solver='adam', tol=0.0001, validation_fraction=0.1, verbose=True,
                    warm_start=False)
clf.fit(X_train, y_train) 
pred = clf.predict(X_test)
print('MLP: ')
print(metrics.accuracy_score(y_test, pred))
joblib.dump(clf, '../models/mlp.pkl')
print("Model Saved")