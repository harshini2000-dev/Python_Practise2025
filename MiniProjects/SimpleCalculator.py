def addition(x,y):
    return x + y

def substraction(x,y):
    return x - y

def product(x,y):
    return x * y

def calculate():
    op = input("Operation (+,-,*) : ")
    num1 = int(input("Number 1: "))
    num2 = int(input("Number 2: "))
    if op == '+':
        return addition(num1,num2)
    elif op == '-':
        return abs(substraction(num1, num2))
    elif op == '*':
        return product(num1,num2)
    else:
        print(f"{op} operation can't be performed")

result = calculate()
print(result)