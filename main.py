import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'type a number from 1 to {x}: '))
        if guess < random_number:
            print("too low")
        elif guess > random_number:
          print("too high")

    print(f"congrats!!!")

guess(100)
