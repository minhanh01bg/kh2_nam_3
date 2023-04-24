from sklearn import svm
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn import linear_model
import pickle

df = pd.read_csv('diabetes.csv')
# print("0s")
# print("==")
# print(df.eq(0).sum())

# ---features---
X = df[['Glucose', 'BMI', 'Age']]
# ---label---
y = df.iloc[:, 8]
log_regress = linear_model.LogisticRegression()
log_regress_score = cross_val_score(log_regress, X, y, cv=10,
                                    scoring='accuracy').mean()
print(log_regress_score)
result = []
result.append(log_regress_score)

``
# ---empty list that will hold cv (cross-validates) scores---
cv_scores = []


# ---number of folds---
folds = 10
# ---creating odd list of K for KNN---
ks = list(range(1, int(len(X) * ((folds - 1)/folds)), 2))
# ---perform k-fold cross validation---
for k in ks:
    knn = KNeighborsClassifier(n_neighbors=k)
    score = cross_val_score(knn, X, y, cv=folds, scoring='accuracy').mean()
    cv_scores.append(score)
# ---get the maximum score---
knn_score = max(cv_scores)
# ---find the optimal k that gives the highest score---
optimal_k = ks[cv_scores.index(knn_score)]
print(f"The optimal number of neighbors is {optimal_k}")
print(knn_score)
result.append(knn_score)
# cleanning 107

linear_svm = svm.SVC(kernel='linear')
linear_svm_score = cross_val_score(linear_svm, X, y,
                                cv=10, scoring='accuracy').mean()
print(linear_svm_score)
result.append(linear_svm_score)

rbf = svm.SVC(kernel='rbf')
rbf_score = cross_val_score(rbf, X, y, cv=10, scoring='accuracy').mean()
print(rbf_score)
result.append(rbf_score)


algorithms = ["Logistic Regression", "K Nearest Neighbors",
            "SVM Linear Kernel", "SVM RBF Kernel"]
cv_mean = pd.DataFrame(result, index=algorithms)
cv_mean.columns = ["Accuracy"]
cv_mean.sort_values(by="Accuracy", ascending=False)

# knn = KNeighborsClassifier(n_neighbors=19)
# knn.fit(X, y)


# ---save the model to disk---
# filename = 'diabetes.sav'
# #---write to the file using write and binary mode---
# pickle.dump(knn, open(filename, 'wb'))
# loaded_model = pickle.load(open(filename, 'rb'))
# df.info()
# print("Nulls")
# print("=====")
# print(df.isnull().sum())
# ---check for 0s---
# print("0s")
# print("==")
# print(df.eq(0).sum())
