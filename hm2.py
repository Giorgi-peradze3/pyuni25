x = float(input("subject 1: "))
y = float(input("subject 2: "))
c = float(input("subject 3: "))
d = float(input("subject 4: "))
f = float(input("subject 5: "))
g = float(input("subject 6: "))

avg = (x + y + c + d + f + g) / 6

if avg >= 91 and avg <= 100:
    print("A")
elif avg >= 81:
    print("B")
elif avg >= 71:
    print("C")
elif avg >= 61:
    print("D")
elif avg >= 51:
    print("E")
else:
    print("F")