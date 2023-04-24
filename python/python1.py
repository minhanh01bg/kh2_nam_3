from collections import defaultdict
import wikipedia
import algorithm
from queue import Queue

def sortByFreq(arr, n):
    d = defaultdict(lambda: 0)
    for i in range(n):
        d[arr[i]] += 1
    arr.sort(key = lambda x: (-d[x], x))

    return (arr)

def main():
    t = int(input())
    while t!=0 :
        n = int(input())
        lst = input().split()
        lst = list(map(lambda x: int(x) if x.isdigit() else 0,lst))
        solution = sortByFreq(lst, n)
        print(*solution)
        t -= 1

if __name__ == "__main__":
    main()