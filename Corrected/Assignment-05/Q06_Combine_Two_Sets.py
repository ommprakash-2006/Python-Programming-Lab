# The manual's first-set input statement is missing.
# This input line is inferred from the later use of s1 in the supplied steps.
s1 = set(eval(input("Enter the 1st set: ")))
s2 = set(eval(input("Enter the 2nd set: ")))

s1.update(s2)
s3 = s1
print("After combining the sets:", s3)
