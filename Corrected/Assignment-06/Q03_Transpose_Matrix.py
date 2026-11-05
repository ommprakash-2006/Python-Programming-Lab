rows = int(input("Give the number of rows: "))
columns = int(input("Give the number of columns: "))

if rows <= 0 or columns <= 0:
    print("Rows and columns must be positive.")
else:
    matrix = [
        [int(input(f"Enter element [{r + 1}][{c + 1}]: ")) for c in range(columns)]
        for r in range(rows)
    ]

    print("Original Matrix:")
    for row in matrix:
        print(*row, sep="\t")

    print("Matrix after transpose:")
    for row in zip(*matrix):
        print(*row, sep="\t")
