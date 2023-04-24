# str = input()
import re
# for i in range(31):
#     str = input()
#     str = re.sub("\s+",",",str)
#     print(str)
    
with open("./txt.txt") as f:
    line = f.readline()
    while line:
        print(re.sub("\s+",",",line))
        line =f.readline()
