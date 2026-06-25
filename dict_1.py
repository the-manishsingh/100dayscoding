dic = {}
n = int(input())
for i in range(0,n):
    a = input()
    name,phoneno = a.split()
    dic[name]=phoneno
for i in range(0,n):
    b = input()
    r = ""
    if b in dic:
        r = r + b
        r = r + '='
        r = r + dic[b]
        print(r)
    else:
        print("Not found")
    
    
    
