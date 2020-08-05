# Description: A program to get a list as input and print the 
# first and last element of that list.

def get_list(number_list):  # A function to get a list (parameter = number_list)
    while True:             # A while loop to continuously get input
        number = input("Enter a list of numbers(type '#' to exit): ")   # Input prompt
        if number == '#':       # If input is '#' then stop inputing
            break
        elif number in "0123456789":                   # Otherwise,
            number = int(number)    # Convert input to an integer
            number_list.append(number)  #then, append that number to number_list
        else:
            print("Invalid input.")
        
number_list = []
try:
    get_list(number_list)
    print(f"First element = {number_list[0]} and Last element = {number_list[-1]}")
except IndexError:
    print("No element in list.")
except ValueError:
    print("Nothing was entered.")