# assign value to a variable

full_name = 'Sai Harshini Pasupuleti' # python is a type inferred lang - means no need to mention variable type
print(full_name)
print(id(full_name))
# change value 

full_name = 'Sai Druthi'
print(full_name)
print(id(full_name)) # points to different object now, becomes more clear as we learn in depth in further days

# assign multiple values

a,b,c = 1,2,3
print(a)
print(b)
print(c)

# assign same value to one variable
first_name = middle_name = 'sai'
print(first_name)
print(middle_name)

print(id(first_name))
print(id(middle_name))