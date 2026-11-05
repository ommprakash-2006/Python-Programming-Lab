x = input("Enter a string: ")

print("Reversed words:")
print(" ".join(x.split()[::-1]))

vowels = sum(1 for char in x if char.isalpha() and char.lower() in "aeiou")
consonants = sum(1 for char in x if char.isalpha() and char.lower() not in "aeiou")

print("The vowels are:", vowels)
print("The consonants are:", consonants)
