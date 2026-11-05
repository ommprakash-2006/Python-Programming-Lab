# Iterative Fibonacci avoids the exponential cost of the manual's recursive lambda.
terms = int(input("Enter the number of terms: "))

if terms < 0:
    print("Enter a non-negative number.")
else:
    a, b = 0, 1
    series = []
    for _ in range(terms):
        series.append(a)
        a, b = b, a + b
    print("Fibonacci series:")
    print(*series)
