import random

answer = random.randint(1, 21)

print("Guess the number between 1 and 20")

while True:
    guess = int(input())
    if guess==answer:
        print("{} is the correct answer".format(guess))
        break
    if guess < answer:
        print("Try a larger number")
    elif guess > answer:
        print("Try a smaller number")
