x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

print("Addition is:", x + y)
print("Subtraction is:", x - y)
print("Multiplication is:", x * y)

if y != 0:
    print("Division is:", x / y)
    print("Remainder is:", x % y)
    print("Floor value is:", x // y)
else:
    print("Division, remainder, and floor division are undefined when y is 0.")
