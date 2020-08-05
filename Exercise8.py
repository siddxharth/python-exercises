import random
print("To exit game, press '#'.")
while True:
    computer_choice = ["Scissors","Paper","Rock"]
    computer_choice = computer_choice[random.randint(0,2)].upper()
    user_input = input("What's your move? (Rock/Paper/Scissors)\n").upper()
    print(f"Computer choice: {computer_choice}")
    print(f"Your move: {user_input}")
    print('#########################')
    if user_input == "#":
        break
    elif user_input[0] == computer_choice[0]:
        print("Draw!")
    elif user_input[0] == "S":
        if computer_choice[0] == "P":
            print("You win!!!")
        else:
            print("Computer wins!")
    elif user_input[0] == "P":
        if computer_choice[0] == "S":
            print("Computer wins!")
        else:
            print("You win!!!")
    elif user_input[0] == "R":
        if computer_choice[0] == "P":
            print("Computer wins!")
        else:
            print("You win!!!")
    else:
        print("I don't know what to do with this?!")
    print('#########################')