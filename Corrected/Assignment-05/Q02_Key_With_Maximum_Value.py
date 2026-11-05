import ast

data = ast.literal_eval(input("Enter the dictionary: "))

if not isinstance(data, dict) or not data:
    print("Please enter a non-empty dictionary.")
else:
    key = max(data, key=data.get)
    print("The key with maximum value is:", key)
