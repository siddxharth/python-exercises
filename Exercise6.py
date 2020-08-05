string = input("Enter a string: ")

if string[0:-1] == string[-1:0:-1]:
    print("String is Palindrome.")
else:
    print("String is not Palindrome.")