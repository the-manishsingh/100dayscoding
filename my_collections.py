ns = int(input())
# Returns a list of integers
s = list(map(int, input().split()))
c = int(input())
d = []
r = 0
for i in range(c):
    d.append(list(map(int, input().split())))

for i in d:
    if i[0] in s :
        s.remove(i[0])
        r = r + i[1]


# print(d)
print(r)