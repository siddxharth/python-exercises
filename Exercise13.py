# Description: A program which asks the user for the number 
# of Fibonnaci numbers to generate. 

# Hint: seqence is a sequence of numbers where the next number
# in the sequence is the sum of the previous two numbers in the sequence.
# The sequence looks like this: 1, 1, 2, 3, 5, 8, 13...

# Date: 1 August 2020
#Programmer: Siddharth(t/@siddxharth)

def fibonnaci():
    choice = int(input("How many fibonnaci numbers do you want?\n"))

    fibonnaci = []

    if choice == 0:
        print(fibonnaci)
    elif choice == 1:
        fibonnaci = [1]
        print(fibonnaci)
    elif choice == 2:
        fibonnaci = [1,1]
        print(fibonnaci)
    else:
        fibonnaci = [1,1]
        i = 2
        while i<choice:
            fibonnaci.append(fibonnaci[i-1]+fibonnaci[i-2])
            i+=1
        print(fibonnaci)

fibonnaci()
