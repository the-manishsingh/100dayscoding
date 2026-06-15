z = input()
n,m = z.split(' ')
n = int(n)
m = int(m)
a = []
b = []

for i in range(0,n):
    a.append(input())
for i in range(0,m):
    b.append(input())

for i in b:
    l =''
    f = False
    for q in range(0,len(a)):
        
        if i == a[q]:
            l.join(q+1)
            f = True
    if l != '':
        print(l)
    if f == False : 
        print('-1')