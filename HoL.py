import random as rand
import os

def clear():
    os.system("cls")

while True:
    clear()
    print("Made by Gamerjig")
    #Made by Gamerjig
    print("Number can be from 0 - 100")

    amount = int(input("Enter how many chances you get: "))

    rn = str(rand.randint(0, 100))

    for i in range(amount):
        guess = str(input("Enter your "+ str(i) + " guess: "))
        
        if guess > rn:
            print("Lower")
        elif guess < rn:
            print("Higher")
        else:
            amount = 0
            print("You win!")

        b = i + 1

        print(amount)
        print(str(b))

        if str(b) == str(amount):
            clear()
            print("You lose..")
            print("The number was "+ rn)
    
    print("Play again?")
    print("1 - yes")
    print("2 - No")
    again = str(input("Enter your chose: "))

    if again == "1":
        print("Restarting")
    elif again == "2":
        print("Stopping")
        break
    else:
        print("Must be 1 or 2")