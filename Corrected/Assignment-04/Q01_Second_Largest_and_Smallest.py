values = []
count = int(input("Enter the number of elements: "))

if count < 2:
    print("Enter at least two elements.")
else:
    for _ in range(count):
        values.append(int(input("Enter an element: ")))

    unique_values = sorted(set(values))
    if len(unique_values) < 2:
        print("At least two distinct values are required.")
    else:
        print("Sorted array:", sorted(values))
        print("Second largest element is:", unique_values[-2])
        print("Second smallest element is:", unique_values[1])
