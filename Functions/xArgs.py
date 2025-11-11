# *args
# Arbitary arguments
# sum of many numbers

def sum_of_nums(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    
    print(sum)

sum_of_nums(10,20,30,40,50)
sum_of_nums(300,200)