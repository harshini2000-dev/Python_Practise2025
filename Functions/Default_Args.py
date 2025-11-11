def increaseBy(num, by = 1):   # default arg - by = 1
    return num + by

result1 = increaseBy(10)     # uses 1 for 'by' the default value

result2 = increaseBy(10, 20) # uses 20 for 'by'

print(result1)
print(result2)

'''
default params also known as optional param.
should always come at the end.
'''