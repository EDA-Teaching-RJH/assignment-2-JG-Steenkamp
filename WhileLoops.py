### Part Two -- your code goes here. 
import random

number = random.randint(1,100)

guess = 0

print("Lets play a little game, guess what number I'm thinking of.")

while guess != number:

    guess = int(input('guess: '))
    if guess == number:
        print("You got it!")
        break