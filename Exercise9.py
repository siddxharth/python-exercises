import random

guesses = 0
user_guess = ''
random_number = random.randint(1,10)
while user_guess != 'exit':
    user_guess = input("Guess a number: ")
    guesses += 1
    if int(user_guess) > random_number:
        print("Too high.")
    elif int(user_guess) < random_number:
        print("Too low.")
    else:
        print(f"Exactly right. Number was {random_number}")
        print(f"Guessed in {guesses} tries.")
        guesses = 0
        random_number = random.randint(1,10)
print("You entered something that I can't understand.")