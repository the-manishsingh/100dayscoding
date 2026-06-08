
import os


def solve(s):
    s = list(s)
    s[0] = s[0].upper()
    for i in range(1, len(s)):
        if s[i-1] == ' ':
            s[i] = s[i].upper()
    s = ''.join(s)
    return s
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    result = solve(s)
    print(result)