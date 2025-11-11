'''
print() takes 5 parameters

print(object, sep, end , file, flush)

object = values to be printed
sep = separate the values with a delimiter 
end = \n or \t 
file = default value is sys.stdout means screen
flush = flushed or buffered default value is false
'''
print()
print(120,130,140, sep='+', end='\t')
print(120+130+140)

x,y = 10,20
print('1. x and y are {} and {} respectively'.format(x,y))
print(f'2. x and y are {x} and {y} respectively')

