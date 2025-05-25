#rock paper sicssors game
import random
num = random.randint(1, 3)
print("===================")
print("Rock Paper Scissors")
print("===================")
print("1) ✊")
print("2) ✋")
print("3) ✌️")
num2 = int(input("Pick a number:"))
if num2 ==1 or num2 == 2 or num2 == 3:                      
    if num == 1:
        print("You picked Rock")
        if num2 == 1:
            print("It's a tie!")
        elif num2 == 2:
            print("You lose! Paper beats Rock")
        else:
            print("You win! Rock beats Scissors")
    elif num == 2:
        print("You picked Paper")
        if num2 == 1:
            print("You win! Paper beats Rock")
        elif num2 == 2:
            print("It's a tie!")
        else:
            print("You lose! Scissors beats Paper")
    else:
        print("You picked Scissors")
        if num2 == 1:
            print("You lose! Rock beats Scissors")
        elif num2 == 2:
            print("You win! Scissors beats Paper")
        else:
            print("It's a tie!")    