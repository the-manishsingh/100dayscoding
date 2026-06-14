n = { "one": 1, "two": 2, "three": 3, "four": 4,
    "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
    "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
    "fourteen": 14, "fifteen": 15, "sixteen": 16,
    "seventeen": 17, "eighteen": 18, "nineteen": 19,
    "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
    "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90}
a = {'hundred':100, 'thousand':1000 , 'lakh': 100000 , "crore":10000000}
u = input().lower().split()#['one','thousand','one','hundred','twenty',"two"]


r = 0
t = 0

for i in u :
    if i in n:
        t = t + n[i]
    elif i in a:
        t = t* a[i]
        r = t+r
        t = 0
r = r + t
print(r)

# 'one thousand one hundred twenty'
# 1*1000+1*100+20 + 1
