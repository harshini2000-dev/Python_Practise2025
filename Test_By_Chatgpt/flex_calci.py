def flex_calculator(op, *nums, round_to=None):
    handled_ops = ["add", "multiply", "power"]

    if op not in handled_ops:  # membership operator - not in
        print(f"{op} operation not applicable")
        return 0

    answer = 0

    if op == "add":
        total = 0
        for n in nums:
            total += n
        answer = total
    elif op == "multiply":
        product = 1
        for n in nums:
            product *= n
        answer = product
    elif op == "power":
        if len(nums) >= 2:
            answer = pow(nums[0], nums[1])
        else:
            print("Need at least two numbers for power")
            return 0

    if round_to is not None:  # identity operator - is not
        answer = float(round(answer, round_to))

    print(answer)


flex_calculator("add", 10, 20, 5, round_to = 1)        # ➝ 35.0
flex_calculator("multiply", 2, 3, 4)                 # ➝ 24
flex_calculator("power", 2, 5, 10, round_to= 1)       # ➝ 32.0
    
    
def flex_calculator_gptversion(operation, *args, round_to=None):
    if not args: # no args passed
        return "No numbers provided."

    operation = operation.lower()

    if operation == "add":
        result = sum(args)

    elif operation == "multiply":
        result = 1
        for num in args:
            result *= num

    elif operation == "power":
        if len(args) < 2:
            return "Need at least two numbers for power operation."
        result = args[0] ** args[1]

    else:
        return f"Unsupported operation: {operation}"

    if round_to is not None:
        result = round(result, round_to)

    return result



print(flex_calculator_gptversion("add", 10, 20, 30))               # ➝ 60
print(flex_calculator_gptversion("multiply", 2, 3, 4))             # ➝ 24
print(flex_calculator_gptversion("power", 2, 5, round_to=2))       # ➝ 32.0
print(flex_calculator_gptversion("divide", 10, 2))                 # ➝ Unsupported operation
print(flex_calculator_gptversion("add"))                           # ➝ No numbers provided.
 

    
