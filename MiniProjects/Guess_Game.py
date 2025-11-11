# Small game using while loop

secret = 7
chances = 1
success = False

while chances <= 3:
    guess = int(input("Guess ? "))
    if(guess == secret):
        success = True
        print("Success !")
        break
    chances += 1
else:
    print("Game over!")
    
# if(success == False):
#     print("Game over !")
