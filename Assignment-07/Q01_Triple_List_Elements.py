x=list(eval(input("Enter a list:")))
def triple(x): return x*3
y=list(map(triple,x))
print(y)