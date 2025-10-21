

# Guess game
import random

randm = random.randint(1,100)

attempt = 1
guess = int(input("Enter your guess between 1 to 100: "))

while guess != randm:
    if guess < randm:
        print("guess higher")
    elif guess > randm:
        print("guess lower")
    else:
        print("Invalid input, please enter a number between 1 to 100")
    guess = int(input("Enter your guess between 1 to 100: "))
    attempt += 1

    
print("you gueessed it right! the random no is"  ,randm)
print(f"You took {attempt} attempts to guess the number.")
print("Thank you for playing the game!")
 