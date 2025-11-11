
employee = ("Harshini", 25, "Software Engineering")

# tuple unpacking - assign multiple values at once from the tuple
ename, age, dept = employee

print(ename)
print(age)
print(dept)

# Given this tuple:
info = ("banana", 1.25, "fruit")

# Unpack it into 3 variables:
name, price, category = info
# Then print each variable
print(name, price, category)

# unpacking nested tuples
student = ("Asha", (20, "good_student"))
name, std_details = student

print(name)
print(std_details)

rollno, review = std_details
print(rollno)
print(review)

student = ("Asha", (90, 85, 92))

# Unpack so that:
# name = "Asha"
# scores = 90, 85, 92
sname, scores = student
# Then print the name and all three scores
print(sname)
print(scores)