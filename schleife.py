import random

secret = random.randint(1, 30)
guess = 0
i = 3

for x in range(i):
    try:
        guess = int(input("Guess the secret number (between 1 and 30): "))
    except ValueError:
        print("Please type in a number")
        continue

    if guess == secret:
        print("Yeah!")
        break
    elif guess > secret:
        print("try something smaller")
    elif guess < secret:
        print("Try something bigger")
    i = i + 1

print("Sorry, you lost!")
