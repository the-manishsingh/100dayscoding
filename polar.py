import math
import cmath
z = input()

z = z.replace('j','')

print(z)

for i in range(1,len(z)):
    if z[i] == '+' or z[i] == '-':
        x = z[:i]
        y = z[i:]
print(x,y)

x = int(x)
y = int(y)



rz = math.hypot(x, y)
rz2 = cmath.phase(complex(x, y))
print(rz)
print(rz2)