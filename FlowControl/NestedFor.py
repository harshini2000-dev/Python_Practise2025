iteration = 0
for x in range(5):  # 0,1,2,3,4
    for y in range(3): # 0,1,2
        print(f"({x},{y})")
        iteration += 1
else:
    print(iteration) # 5 * 3 = 15
        
'''
y loop exec 3 times for each iter of x which is 5.
5 * 3 = 15 iterations

x = 0
    y = 0
    y = 1
    y = 2
x = 1
    y = 0 
    y = 1
    y = 2
x = 3 
    y = 0 
    y = 1
    y = 2
...
'''