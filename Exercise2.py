# A program which takes a number as input and prints out if that 
# number is Even or Odd. It also takes another two numbers as 
# input and checks if the first number is completely divisible by
# the second number, it prints appropirate string.
# Date: 30 July 2020
# Programmer: Siddharth(t@siddxharth)

number = int(input("Enter a number: ")) #Take input and convert it into integer

if number%4 == 0:   #Check if the inputed number is evenly dividible by 4
    print("Multiple of 4!!!!")
elif number%2 == 0: #Otherwise, Check if the number is Even
    print("Even!!")
else:               #If number is not Even, number is Odd.
    print("Odd!!!")

num = int(input('Enter a number: '))    #Take another number(Divident) as input

check = int(input('Enter another number: ')) #Take another number(Divisor) as input

if num%check == 0:                        #If Divident is evenly divisible by Divident, print appropirate string.
    print("Num divides evenly by Check.")
else:                                     #Otherwise, print Not Divisible string.
    print("Num doesn't divide evenly by Check.")