import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("./train.csv")

print(df.shape) # (30471, 292)
# tách các cột số khỏi các cột phân loại
# select numerical columns
df_numeric = df.select_dtypes(include=[np.number])
numeric_cols = df_numeric.columns.values
# select non-numeric columns
df_non_numeric = df.select_dtypes(exclude=[np.number])
non_numeric_cols = df_non_numeric.columns.values


# bắt đầu cleaning
# % of values missing in each column
values_list = list()
cols_list = list()
for col in df.columns:
    pct_missing = np.mean(df[col].isnull())*100 # giá trị trung bình của Nan
    cols_list.append(col)
    values_list.append(pct_missing)
pct_missing_df = pd.DataFrame()
pct_missing_df['col'] = cols_list # danh sách cột
pct_missing_df['pct_missing'] = values_list # giá trị trung bình nan trong một cột
# print(cols_list)

# lọc những cột có giá trị > 0 để vẽ 
# pct_missing_df.loc[pct_missing_df.pct_missing> 0].plot (kind = 'bar', figsize = (12,8)) 
# plt.show ()


# Drop observations
# tìm những cột có tỉ lệ giá trị nan rất thấp
less_missing_values_cols_list = list(pct_missing_df.loc[(pct_missing_df.pct_missing < 0.5) & (pct_missing_df.pct_missing > 0), 'col'].values)
df.dropna(subset=less_missing_values_cols_list, inplace=True) #xóa các hàng có giá trị nan trong các cột có rất ít giá trị nan(null)

print(less_missing_values_cols_list)
print(df.shape) # (30446, 292)


#Remove columns (features)
# tìm những cột có giá trị nan > 40% và xóa cột đó
_40_pct_missing_cols_list = list(pct_missing_df.loc[pct_missing_df.pct_missing > 40, 'col'].values)
df.drop(columns=_40_pct_missing_cols_list, inplace=True)
print(df.shape) #(30446, 286)



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
             
# print(df.isnull().sum()) # tổng số giá trị nan trong 1 cột
# print(df.isnull().sum().sum()) # tổng số giá trị nan trong toàn bộ 



# ngoại lệ(những giá trị bất thường)
print(df.life_sq.describe ())
# xóa giá trị bất thường là 7478 trong cột life_sq
df = df.loc [df.life_sq <7478]



# Xóa bản ghi của dữ liệu bị trùng

# giảm trùng lặp bằng cách xem xét tất cả các cột ngoài ID 
cols_other_than_id = list(df.columns)[1:] #cột id là cột 1
df.drop_duplicates(subset = cols_other_than_id, inplace = True) # xóa trùng lặp



# sửa kiểu dữ liệu

print(df.timestamp.dtype) #object
df['timestamp'] = pd.to_datetime(df.timestamp, format='%Y-%m-%d') # format lại thành datetime theo định dạng ngày tháng năm
print(df.timestamp.dtype) #datetime
