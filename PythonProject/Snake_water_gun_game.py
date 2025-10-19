import random
"""Snake Water Gun Game
Snake vs Water = Snake wins
Water vs Gun = Water wins
Gun vs Snake = Gun wins
    """
s = 0
w = 1
g = 2

inp = int(input("Enter your gesture-number(0 = snake , 1 = water, 2 = gun): "))
print(f"You chose {inp}")

computer = random.randint(0,2)
print(f"Computer chose {computer}")


def draw(s,w,g):
    inp == s and computer == 0
    inp == w and computer == 1
    inp == g and computer == 2


def win_lose(s,w,g):
    if inp == s and computer == 1:
        print("congrats snake you win over water")
    elif inp == w and computer == 2 :
        print("congrats water you win over gun")
    elif inp == g and computer == 0 :
        print("congrats gun you win over snake")
    elif computer == s and inp == 1:
        print("computer chose snake and wins over water")
    elif computer == w and inp == 2 :
        print("computer chose water and wins over gun")
    elif computer == g and inp == 0 :
        print("computer chose gun and wins over snake")

if draw(s,w,g):
    print("It's a draw")
elif win_lose(s,w,g):
    win_lose(s,w,g)
else:
    print("Invalid input! Please choose a number between 0 and 2.")









