# Write a function power(base, exponent=2) that returns the result of base raised to the power of exponent.
# If exponent is not provided, it should square the base.

def power(base, exp = 2):
    return base ** exp

res = power(3,3)
print(res)