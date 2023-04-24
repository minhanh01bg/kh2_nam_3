# các cách xử lý dữ liệu bị bỏ trống trong file csv
import pandas as pd
import numpy as np
df = pd.read_csv('./aud-jpy-(1d) (5).csv')
print(df.head())
print(df.isnull().sum())

# print(df.eq(0).sum())

# df[['DateTime','AUD/JPY (open)','AUD/JPY (high)',
#  'AUD/JPY (low)','AUD/JPY (close)','Navigator']] = \
#  df[['DateTime','AUD/JPY (open)','AUD/JPY (high)',
#  'AUD/JPY (low)','AUD/JPY (close)','Navigator']].replace(0,np.NaN)

print(df.head())
# kết quả sau khi replace
print(df.eq(0).sum())

# thay thế giá trị NaN thành giá trị trung bình của cột đó
df.fillna(df.mean(), inplace = True)
print(df.head())