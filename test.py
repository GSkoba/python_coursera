print("hello")

num = 100_000_000

print(type(num))

num = 13.4

print(num)

num = -10.45

print(num)

num = -21.4

print(num)

print(type(num))

num = 1.5e2

print(num)

print(type(num))

num = int(num)

print(num, type(num))

num = float(num)

print(num, type(num))

num = 14 + 1j

print(num)

print(type(num))

print(num.real)

print(num.imag)

x1, y1 = 0, 0
x2, y2 = 3,4
distance = ((x2-x1)**2+(y2-y1)**2)**0.5
print(distance)

result = True
print(result, type(result))

x = 2
print(1<x<3)

x = -2
print(bool(x))

a, b = 1, 2
print(a,b)
a,b=b,a
print(a,b)

x, y = True, False
print(x and y)

print(x or y)

print(not(y))

year = 2017
#Ленивые логические операции
is_leap = year % 4 ==0 and (year % 100 != 0 or year % 400 != 0)
print(is_leap)

import calendar

print(calendar.isleap(2016))