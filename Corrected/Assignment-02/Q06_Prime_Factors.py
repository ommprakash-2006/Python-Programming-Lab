x = int(input("Enter a positive integer: "))

if x < 2:
    print("No prime factors.")
else:
    factor = 2
    while factor * factor <= x:
        while x % factor == 0:
            print(factor, end=" ")
            x //= factor
        factor += 1
    if x > 1:
        print(x, end="")
    print()
