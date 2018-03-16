import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

x1 = (-b - (b**2-4*a*c)**0.5)/(2*a)
x2 = (-b + (b**2-4*a*c)**0.5)/(2*a)

x1, x2 = int(x1), int(x2)

print(x1)
print(x2)