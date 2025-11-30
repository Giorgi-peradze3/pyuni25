number = float(input("enter number: "))
grades = float(input("enter grades: "))
grades2 = float(input("enter grades: "))



if grades2 > grades:
     print(grades2,'is bigger')
     print(grades,'is smallest')
     print((grades2 + grades) / 2)
elif grades > grades2:
    print(grades,'is bigger')
    print(grades2,'is smallest')
    print((grades + grades2) / 2)