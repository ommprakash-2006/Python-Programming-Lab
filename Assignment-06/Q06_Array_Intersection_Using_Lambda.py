array1=list(eval(input("Enter the 1st list:")))
array2=list(eval(input("Enter the 2nd list:")))
intersection=list(filter(lambda x:x in array1,array2))
print("Intersection of array1 & array2 is: ",intersection)