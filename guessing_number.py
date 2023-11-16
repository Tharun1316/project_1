import random
number = random.randint(1,100)
guess = 0
while guess != number:
    guess = int(input("Enter guessing number between 1-100 : "))
    if guess < number:
        print("Guess higher number")
    elif guess > number:
        print("Guess lower number")
    else:
        print("Yay! Congratulations...YOU WON")