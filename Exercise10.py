# A program to return a list that contains only the elements
# that are common between two given lists.
# Date: 1 August 2020
# Programmer: Siddharth(t/@siddxharth)

# Let the two given strings be:
a = [1, 1, 2, 3, 99, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 99, 7, 8, 9, 10, 11, 12, 13]

# Declaring and assigning common elements in list 'a' and 'b' to list 'c'
c = [element for element in a and b if element in a and b]

# Printing list 'c'
print(c)