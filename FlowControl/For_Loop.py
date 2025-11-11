for num in range(3): # 0 to 2
    print("Calling user", num + 1, (num + 1) * ".")

print(10 * "Ammu ")

for num in range(1,4): # 1 to 3
    print("Attempt ", num, num * ".")

for num in range(1,10,2): # step = 2
    print("Sending msg ", num)

for x in range(1,10):
    if x % 2 == 0:
        print(x ," even")
    else: 
        continue
        # if x == 7:
        #     break
else: 
    # if break exec, else won't exec. 
    # else execs only on smooth exit
    print("Loop ends here")