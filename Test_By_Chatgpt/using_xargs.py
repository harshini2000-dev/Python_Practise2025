# Write a function sum_all(*args) that accepts any number of numeric arguments and returns their total sum.

def sum_all(*nums):
    sum = 0
    for n in nums:
        sum += n
    print(sum)

sum_all(10,20,30)