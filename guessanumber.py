import random

secret_number = random.randint(0, 10)

guess_count = 0
guess_limit = 3

while (guess_count < guess_limit):
    guess = int(input("enter a number between 0 to 10:"))
    guess_count += 1
    if (guess == secret_number):
        print("you won")
        break;
else:
    print("good try")
