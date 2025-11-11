# age between 18 to 60
age = 45
if age >= 18 and age <= 60:
    print(f"{age} is okay")
else: 
    print(f"{age} is NOT okay")

# chaining comparison operators: easier version of above code
if(18 <= age <= 60 ):
     print(f"{age} is good")
else:
    print(age, " Not good")