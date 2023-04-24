
def main():
    s = str(input())
    str1 = ""
    k = int(0)
    while True:
        str1 = ""
        str2 = ""
        for i in range(0, int(len(s) / 2)):
            str1 = str1 + s[i]
        for i in range(int(len(s)/2), int(len(s))):
            str2 += s[i]
            
        if(len(str1+str2) <= 1): 
            return
        k = int(str1) + int(str2)
        print(k)
        s = str(int(str1)+int(str2))
    

if __name__ == "__main__":
    main()