n = int(input())
name = input().split()
a = []
f = 0
r = 0
for i in range(0,n):
    a.append(input().split())
for i in range(0,4):
    if name[i] == 'MARKS':
        f = i     
for i in range(0,n):
    r = r + int(a[i][f])
    
print(r/n)


# input type
# 5
# ID         MARKS      NAME       CLASS     
# 1          97         Raymond    7         
# 2          50         Steven     4         
# 3          91         Adrian     9         
# 4          72         Stewart    5         
# 5          80         Peter      6 