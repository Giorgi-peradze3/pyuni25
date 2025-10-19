a = int(input())
b = int(input())
c = int(input())

x = a
if a > b and a > c:
    x = a
elif b > a and b > c:
    x = b
elif c > a and c > b:
    x = c

y = a
if a < b and a < c:
    y = a
elif b < a and b < c:
   y = b
elif c < a and c < b:
    y = c

z = a
if a != x and a != y:
    z = a
elif b != x and b != y:
    z = b
elif c != x and c != y:
    z = c

print(y,z,x)