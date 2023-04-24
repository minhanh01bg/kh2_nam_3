import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("./w33.csv")

print(df.isnull().sum())

# đối với cột giá trị là số, thay thế nan = mean() của cột đó
df_numeric = df.select_dtypes(include=[np.number])
numeric_cols = df_numeric.columns.values
for col in numeric_cols:
    missing = df[col].isnull()
    # print(df[col].isnull().sum())
    num_missing = np.sum(missing) # tổng các số nan trong 1 cột
    # print(num_missing)
    if num_missing > 0:  # impute values only for columns that have missing values
        med = df[col].median() #impute with the median
        df[col] = df[col].fillna(med) #thay thế nan bằng giá trị trung bình
        
# đối với cột phân loại(ko phải giá trị số)
df_non_numeric = df.select_dtypes(exclude=[np.number])
non_numeric_cols = df_non_numeric.columns.values
for col in non_numeric_cols:
    missing = df[col].isnull()
    num_missing = np.sum(missing)
    if num_missing > 0:  # impute values only for columns that have missing values
        mod = df[col].describe()['top'] # impute with the most frequently occuring value(giá trị thường gặp nhất)
        df[col] = df[col].fillna(mod) #thay thế nan bằng giá trị thường gặp nhất trong cột đó
             
print(df.isnull().sum()) # tổng số giá trị nan trong 1 cột
# print(df.isnull().sum().sum()) # tổng số giá trị nan trong toàn bộ 

# df.dropna(inplace = True) # drop NaN


#drop duplicates
cols_other_than_id = list(df.columns)
df.drop_duplicates(subset=cols_other_than_id,inplace=True)
print(df)

# convert to date for date column
print(df.Date.dtype)
df['Date'] = pd.to_datetime(df['Date'])
print(df.Date.dtype)
# print(df)

df.to_csv("./after.csv")