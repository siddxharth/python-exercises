# Description: A program which takes a number as input from user
# and determines if it is a prime number or not.
# Date: 1 August 2020
# Programmer: Siddharth(t/@siddxharth)

def is_prime(number=2):
    loop = 1
    divisors = []
    while loop<=number:
        if number%loop==0:
            divisors.append(loop)
        loop += 1
    if len(divisors)==2:
        return True
    else:
        print(f"Divisors of {number}: {divisors}")
        return False

number = input("Enter a number: ")
number = int(number)
print(is_prime(number))