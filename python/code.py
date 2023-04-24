import algorithm
import math
def isPrime(n):
    Sp = int(math.sqrt(n))
    for i in range (2,Sp+1):
        if n % i == 0:
            return False
    return True

def main():
    n = int(input())
    for i in range (2,n):
        if isPrime(i):
            print(i)
            # Str = Str + str(i) + " "
if __name__ == "__main__":
    main()