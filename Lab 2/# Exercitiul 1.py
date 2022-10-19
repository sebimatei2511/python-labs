# Exercitiul 1
# Write a function to return a list of the first n numbers in the Fibonacci string.

def fibonacci_number(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci_number(number - 2) + fibonacci_number(number - 1)

print("Please write a positive number:")
input = input()

for i in range (0, int(input)):
    print(fibonacci_number(i), end = " ")