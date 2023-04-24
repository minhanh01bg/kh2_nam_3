#1.dao nguoc chuoi
# my_string = "ABCDEFG"
# reversed_string = my_string[::-1]
# print(reversed_string)

#2.xoa cac phan tu giong nhau
# my_string = "aaaabcccccddd"
# temp_set = set(my_string)
# new_string = "".join(temp_set)
# print(new_string)

#3. Viet hoa ki tu dau tien
# my_string = "viet hoa ki tu dau tien"
# new_string = my_string.title()
# print(new_string)

#4. in một chuỗi hoặc 1 list n lần
# n = 3
# my_string = "abc"
# my_list = [1, 2, 3]
# print(my_string*n)
# print(my_list*n)

#5.list comprehension
# my_list = [1,2,3]
# new_list = [2*x for x in my_list]
# print(new_list)

#6.Hoán đổi giá tri giữa hai biến trong python
# a=1
# b=2
# a, b = b, a
# print(a)
# print(b)

#7. tách 1 chuỗi thành 1 danh sách
## tách mặc định từ khoảng trắng
# string_1 = "tên tôi là vũ minh anh"
# print(string_1.split())
# string_2 = "chuỗi 1/ chuỗi 2"
# # tách chuỗi từ dẫu /
# print(string_2.split('/'))

#8.kết hợp mảng chuỗi thành 1 chuỗi
#sử dụng join
#list_of_my_string = ['tên','tôi','là','vũ','minh','anh']
#print(' '.join(list_of_my_string))

#9.kiểm tra 1 chuỗi có phải là chuỗi đối xứng
#sử dụng đảo ngược chuỗi
# my_string = 'abcba'
# if my_string == my_string[::-1]:
#     print('chuỗi đối xứng')
# else:
#     print('chuỗi không đối xứng')

#10.tìm số lần xuất hiện của các phần tử trong 1 list
# Tìm số lần xuất hiện của mỗi phần từ trong List

# import Counter
# from collections import Counter
# my_list = ['a','a','b','b','b','c','d','d','d','d','d']
# count = Counter(my_list) # Xác định đối tượng counter
# print(count) # In thông tin tất cả
# Counter({'d': 5, 'b': 3, 'a': 2, 'c': 1})
# print(count['b']) # Số lần xuất hiện của phần tử cụ thể
# 3
# print(count.most_common(1)) # Phần tử xuất hiện nhiều nhất
# [('d', 5)]
