# HACK 2
from  itertools import permutations
u = input().split()
s = u[0]
n = int(u[1])
l = []
p = (list(permutations(s,n)))
for i in p:
    a = ''.join(i)
    l.append(a)
for i in sorted(l) :
    print(i)
