# Các bước cơ bản data clean:
# Bước 1: Xóa lặp lặp giá trị hoặc không liên quan.
# Bước 2: Chỉnh sửa cấu trúc lỗi.
# Bước 3: Lọc các ngoại lệ không mong muốn.
# Bước 4: Xử lý thiếu dữ liệu.
# Bước 5: Xác thực và đảm bảo chất lượng.


import pandas as pd
df = pd.read_csv('./duplicate.csv')
print(df)
print(df.duplicated(keep=False))
df.drop_duplicates(subset=['A', 'C'], keep='last',inplace=True) # remove all duplicates in
 # columns A and C and keep
 # the last
print(df)
