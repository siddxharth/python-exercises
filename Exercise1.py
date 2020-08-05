# A program that takes user's name as input and prints out the 
# year in which they will be 100 years old. 
# Date: 30 July 2020
# Programmer: Siddharth(t@siddxharth)

name = input("Enter your name: ")
age = int(input("Enter your age: "))

copies = int(input("How many copies you want? "))

current_year = 2020
year_when_100 = current_year+(100-age)

print(copies*f"{name}, in {year_when_100} ({100-age} years), you will be 100 years old.\n")