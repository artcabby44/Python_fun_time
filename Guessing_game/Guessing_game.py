import random


number = random.randint(1,10)
print("Do you want to play a guessing game? Yes or No?")
challenge = input()
challLower = challenge.lower()

if challLower == "yes":
    print("First let me know your name, What's your name? ")
    players_name = input()
    
    print("Okay " + players_name + " let's play I have a number between 1-10, You have 5 tries to guess my number..")
    print("Enter your number: ")
    guesses = 5
    while guesses != 0:
        guess = int(input())
        guesses -= 1
        RigthGuess = 5 - guesses
        if guess > number:
            print("Your guess it too high, You have " + str(guesses) + " trial left")
        elif guess < number:
            print("Your guess it too low, You have " + str(guesses) + " trial left")
        elif guess == number:
            break
    if guess == number:
        print("My number is " + str(number) + " you guess is right, you get it in " + str(RigthGuess) + " guesses")
    else:
        print("Opps.. you have used your 5 trials my number is " + str(number))

else:
    print("Okay, Edi dont! ")
    







            
    
       
        

