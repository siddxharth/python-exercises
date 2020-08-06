import random

choice = input("Enter type of password(\"Easy/Medium/Hard)")
choice = choice.lower()
password = int(input("Enter length of password: "))
numbers = ['1','2','3','4','5','6','7','8','9','0']
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
special = ['!','@','#','$','%','^','&','*','(',')','_','+','/']

character = ''
generated = ''
flag = 1

if choice == "h":
    while flag<=password:
        rand = random.randint(1,3)
        if rand == 1:
            character = numbers
        elif rand == 2:
            character = letters
        else:
            character = special      
        
        element = random.choice(character)
        generated += element
        flag+=1
elif choice == "m":
    while flag<=password:
        rand = random.randint(1,2)
        if rand == 1:
            character = numbers
        else:
            character = letters 
        element = random.choice(character)
        generated += element
        flag+=1
elif choice == "e":
    while flag<=password:
        character = letters 
        element = random.choice(character)
        generated += element
        flag+=1
else:
    print("Invalid password choice.")
print(generated)