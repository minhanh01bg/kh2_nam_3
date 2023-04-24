import pandas as pd
import numpy as np
df = pd.read_csv("./diabetes.csv")
#---check for null values---
print("Nulls")
print("=====")
print(df.isnull().sum())

#---check for 0s---
# giá trị bị trống chỉ ra rằng các giá trị này ko được ghi lại trong tập dữ liệu
# cách đơn giản là thay thế nó thành NaN
print("0s")
print("==")
print(df.eq(0).sum())

df[['Glucose', 'BloodPressure', 'SkinThickness',
    'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']] = \
    df[['Glucose', 'BloodPressure', 'SkinThickness',
        'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']].replace(0, np.NaN)

df.fillna(df.mean(), inplace=True)
# kiểm tra lại sau khi replace 0s->NaN
print(df.eq(0).sum())

# hàm corr tính toán sự tương đồng giữa các cặp đặc điểm
# ex: kết quả cho thấy xét nghiệm dung nạp glucose ít liên quan đến số lần mang thai của một bệnh nhân(prenancies) khoảng 0.127911,nhưng lại có mối quan hệ đáng kể đến outcome(kết quả) khoảng 0.492928
corr = df.corr()
print(corr)
#                           Pregnancies   Glucose  BloodPressure  ...  DiabetesPedigreeFunction       Age   Outcome
# Pregnancies                  1.000000  0.127911       0.208522  ...                 -0.033523  0.544341  0.221898
# Glucose                      0.127911  1.000000       0.218367  ...                  0.137060  0.266534  0.492928
# BloodPressure                0.208522  0.218367       1.000000  ...                 -0.002763  0.324595  0.166074
# SkinThickness                0.082989  0.192991       0.192816  ...                  0.100966  0.127872  0.215299
# Insulin                      0.056027  0.420157       0.072517  ...                  0.098634  0.136734  0.214411
# BMI                          0.021565  0.230941       0.281268  ...                  0.153400  0.025519  0.311924
# DiabetesPedigreeFunction    -0.033523  0.137060      -0.002763  ...                  1.000000  0.033561  0.173844
# Age                          0.544341  0.266534       0.324595  ...                  0.033561  1.000000  0.238356
# Outcome                      0.221898  0.492928       0.166074  ...                  0.173844  0.238356  1.000000

# mục đích ở đây là tìm những đặc điểm ảnh hưởng đáng kể đến kết quả
# sau khi vẽ biểu đồ bằng matplotlib thì ngoài outcome feature, 3 tính năng có ảnh hưởng nhất(influential) là glucose, BMI and Age

# Logistic Regression là thuật toán có giám sát sử dụng để phân lớp
# khi sử dụng thì kết quả đầu ra sẽ trong đoạn [0,1] và 0.5 là ngưỡng để phân loại

# K-NN ngoài việc sử dụng xác thực chéo 10 lần thì còn thử thêm các giá trị khác của k để tìm được k tối ưu nhất để có được accuracy tốt nhất
# KNN là một thuật toán tương đối đơn giản so với các thuật toán khác mà chúng ta đã thảo luận trong các chương trước. 
# Nó hoạt động bằng cách so sánh khoảng cách của phiên bản truy vấn với các mẫu đào tạo khác và chọn K-láng giềng gần nhất. 
# Sau đó, phần lớn các lớp K-láng giềng này là dự đoán của cá thể truy vấn(instance). 
# Hình 9.1 tóm tắt điều này một cách độc đáo. 
# Khi k = 3, ba lân cận gần nhất của hình tròn là hai hình vuông và một hình tam giác. Dựa trên quy tắc đơn giản của đa số, hình tròn được phân loại là hình vuông.
# Nếu k = 5, thì năm hình gần nhất là hai hình vuông và ba hình tam giác. Do đó, hình tròn được phân loại là hình tam giác.

# Support Vector Machines cũng là thuật toán có giám sát và để phân loại
# ý tưởng chính là vẽ một đường thẳng giữa 2 hoặc nhiều lớp theo cách tốt nhất
# kernels: nhân







