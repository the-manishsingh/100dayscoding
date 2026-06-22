#!/bin/python3
#prints greatest continues 1's



if __name__ == '__main__':
    n = int(input().strip())
    b = bin(n)
    a = b[2:]
    a = a.split('0')
    r = 0
    for i in range(1,len(a)):
        if a[r] < a[i]:
            r = i
    print(len(a[r]))

