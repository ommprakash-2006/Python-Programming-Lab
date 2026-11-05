import math

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

if min(a, b, c) <= 0 or a + b <= c or a + c <= b or b + c <= a:
    print("Invalid triangle sides.")
else:
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("Area of triangle is:", area)
