turn = 1
while turn <= 5:
    print(turn)
    turn += 1
else: # smooth exit
    print(turn) # 6 is not <= 5
print("Done")


print("Pattern print: ")   
turn = 1
while turn <= 5:
    print("*" * turn)
    turn += 1

# refer Guess_Game.py