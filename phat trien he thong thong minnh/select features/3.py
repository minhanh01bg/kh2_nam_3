# import pandas as pd
# import numpy as np
# from sklearn.feature_selection import SelectKBest
# from sklearn.feature_selection import chi2
# data = pd.read_csv("./diabetes.csv")
# X = data.iloc[:,:-1]  #independent columns
# y = data.iloc[:,-1]    #target column i.e price range
# #apply SelectKBest class to extract top 10 best features
# bestfeatures = SelectKBest(score_func=chi2, k=8) #chi2 là bộ thử nghiệm không âm để chọn ra k thuộc tính tốt nhất
# fit = bestfeatures.fit(X,y)
# dfscores = pd.DataFrame(fit.scores_)
# dfcolumns = pd.DataFrame(X.columns)
# #concat two dataframes for better visualization 
# featureScores = pd.concat([dfcolumns,dfscores],axis=1) #concat để ghép: axis=1 ghép cột, axis=0 ghép hàng
# featureScores.columns = ['Specs','Score']  #naming the dataframe columns
# print(featureScores.nlargest(4,'Score'))  #print 10 best features

import pandas as pd
import numpy as np
data = pd.read_csv("./diabetes.csv")
X = data.iloc[:,0:20]  #independent columns
y = data.iloc[:,-1]    #target column i.e price range
from sklearn.ensemble import ExtraTreesClassifier
import matplotlib.pyplot as plt
model = ExtraTreesClassifier()
model.fit(X,y)
print(model.feature_importances_) #use inbuilt class feature_importances of tree based classifiers
#plot graph of feature importances for better visualization
print(X.columns)
feat_importances = pd.Series(model.feature_importances_, index=X.columns)
feat_importances.nlargest(10).plot(kind='barh')
plt.show()