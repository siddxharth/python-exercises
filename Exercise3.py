a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = []

number = int(input("Enter a number: "))
[b.append(element) for element in a if element < number]

print(b)