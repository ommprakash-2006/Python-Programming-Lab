x = int(input("Enter a number: "))

if x <= 1:
    print("It is not a perfect number")
else:
    total = sum(i for i in range(1, x) if x % i == 0)
    if total == x:
        print("It is a perfect number")
    else:
        print("It is not a perfect number")
