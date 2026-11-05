def swap(y):
 if y.isupper(): return str(y).lower()
 else: return str(y).upper()
y=list(eval(input("Enter the character list:")))
s=map(swap,y)
print(set(s))