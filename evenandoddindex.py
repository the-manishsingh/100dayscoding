t = int(input())
for i in range(0,t):
    s = input()
    l = len(s)
    e = ""
    o = ""
    for z in range(0,l):
        if z % 2 == 0:
            e = e + s[z]
        else :
            o = o + s[z]
    print(e,o)