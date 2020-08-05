import random

password = int(input("Enter length of password: "))
numbers = ['1','2','3','4','5','6','7','8','9','0']
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
special = ['!','@','#','$','%','^','&','*','(',')','_','+','/']

character = ''
generated = ''
flag = 1

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

print(generated)