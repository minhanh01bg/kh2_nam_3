# # train-test split evaluation random forest on the sonar dataset
# from pandas import read_csv
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score
# # load dataset
# url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/sonar.csv'
# dataframe = read_csv(url, header=None)
# data = dataframe.values
# # split into inputs and outputs
# X, y = data[:, :-1], data[:, -1]
# print(X.shape, y.shape)
# # split into train test sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=1)
# print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)
# # fit the model
# model = RandomForestClassifier(random_state=1)
# model.fit(X_train, y_train)
# # make predictions
# yhat = model.predict(X_test)
# # evaluate predictions
# acc = accuracy_score(y_test, yhat)
# print('Accuracy: %.3f' % acc)

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
# importing data
df = pd.read_csv('headbrain1.csv')
# head of the data
print(df.head())
X = df.iloc[:, :-1] # all rows, all the features and no labels
y = df.iloc[:, -1] # all rows, label only
# using the the train test split function
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                  random_state = 104,
                                  # test_size = 0.25,
                                train_size=0.8,
                                  shuffle = True)
# printing out train and test sets 
print('X_train : ')
print(X_train.head())
print('')
print('X_test : ')
print(X_test.head())
print('')
print('y_train : ')
print(y_train.head())
print('')
print('y_test : ')
print(y_test.head())     
