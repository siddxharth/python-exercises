import random

size_of_a = int(input("Enter size of a: "))
size_of_b = int(input("Enter size of b: "))

a = random.sample(range(0,100),size_of_a)
b = random.sample(range(0,100),size_of_b)

c = [element for element in a and b if element in a and b]

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")