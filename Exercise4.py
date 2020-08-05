number = int(input("Enter a number: "))

list_of_num = range(1,number+1)

divisors = []

for element in list_of_num:
    if number%element==0:
        divisors.append(element)
    element+=1

print(f"Divisors of {number} are " + str(divisors))

if len(divisors) == 2:
    print("and is a prime number.")