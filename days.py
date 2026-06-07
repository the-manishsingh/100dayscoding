import calendar
u = input()
m,d,y=u.split(' ')
d = int(d)
m=int(m)
y=int(y)

r = calendar.weekday(y,m,d) 
print(calendar.day_name[r].upper())