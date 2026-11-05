def fibonacci(n):
    if n <= 0:
        return []
    series = [0, 1]
    while len(series) < n:
        series.append(series[-1] + series[-2])
    return series[:n]


n = int(input("Enter the number of terms you want to print: "))
if n < 0:
    print("Enter a non-negative number.")
else:
    print("The Fibonacci series of first", n, "terms are:")
    print(*fibonacci(n))
