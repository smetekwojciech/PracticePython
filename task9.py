# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

import random

number=random.randint(1,9)
user_number=0
guesses_number=0
while number!=user_number:
    user_input=input("Please guess the number 1-9 or type \"exit\"...\n")
    guesses_number+=1
    if user_input=="exit":
        print("You have exited the program.")
        break
    user_number=int(user_input)
    if number==user_number:
        print("You guessed right! It took you "+str(guesses_number)+" guesses to do it right!")
    elif number>user_number:
        print("You guessed too low!")
    elif number<user_number:
        print("You guessed too high!")