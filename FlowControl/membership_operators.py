# in , not in

# used to test whether a value or variable is found in a sequence (string, list, tuple, set and dictionary).

mylist = [10,20,30,50]

print(10 in mylist )
print(40 in mylist )
print(40 not in mylist)

print('H' in 'Hello World')


dict1 = {1:'a', 2:'b'}

print(1 in dict1)    # True
print('a' in dict1)  # False - checks only in keys