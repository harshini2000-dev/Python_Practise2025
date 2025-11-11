# Convert Int to Float IMplicit conversion

numint = 135
numfloat = 1.35

result = numint + numfloat
print(f'result is {result} which is of {type(result)}')

print()
# python converted small datatype (int) to large datatype (float) to avoid data loss.

# type error for joining string and int 'str' + 12

# Explicict conversion - Type Casting
# use built in functions to change the datatype like str().int(), etc..

print('Explicit Type Casting : \n')
numstr = '21'
newnum = int(numstr)
print(type(newnum))

numint1 = 61
print( 21 + int(numstr))  # 21 + 21 = 42  Sum
print( str(numint1) + numstr)  # '61' + '21' = 6121 concatenate


