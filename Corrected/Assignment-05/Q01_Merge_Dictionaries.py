import ast

dict1 = ast.literal_eval(input("Enter the first dictionary: "))
dict2 = ast.literal_eval(input("Enter the second dictionary: "))

if not isinstance(dict1, dict) or not isinstance(dict2, dict):
    print("Please enter valid dictionaries.")
else:
    merged = dict1.copy()
    merged.update(dict2)
    print("After merging the dictionaries:")
    print(merged)
