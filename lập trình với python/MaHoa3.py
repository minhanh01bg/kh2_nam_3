def sum(s):
    total = 0
    for i in s:
        total += code[i]
    return total


def rotate(s):
    quay = sum(s)
    replace = ""
    for i in range(len(s)):
        replace += (inv_code[((code[s[i]]+quay) % 26)])
    return replace


def merge(s1, s2):
    result = ""
    for i in range(len(s1)):
        result += inv_code[(code[s1[i]] + code[s2[i]]) % 26]
    return result


t = int(input())
while t > 0:
    s = input()
    s1 = s[0:(int)(len(s)/2)]
    s2 = s[(int)(len(s)/2): len(s)]

    code = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12,
            'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

    inv_code = {v: k for k, v in code.items()}

    s3 = rotate(s1)
    s4 = rotate(s2)
    print(merge(s3, s4))

    t -= 1
