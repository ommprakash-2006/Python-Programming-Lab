words = input("Enter a string: ").split()

for word in words:
    if len(word) % 2 == 0:
        print(word)
