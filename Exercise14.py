# Description: A programs that takes a list as input and 
# remove any duplicates from the inputted list.

# Date: 1 August 2020
# Programmer: Siddharth(t/@siddxharth)

def get_list():
    global a_list
    a_list = []
    while True:
        num = input("Enter a list: ")
        if num == '#':
            break
        else:
            a_list.append(int(num))
    return a_list

def rm_duplicates(a_list):
        a_list = set(a_list)           
        return a_list

get_list()
print(rm_duplicates(a_list))