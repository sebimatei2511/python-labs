# Exercitiul 2
#  Write a function that receives a list of numbers and returns 
# a list of the prime numbers found in it.

def prime_bool(number):
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range (3, number // 2, 2):
        if number % i == 0:
            return False
    return True

vector = []
primes = []

length = int(input("Please write the length of the list:"))
print("Please write a list of numbers:")

for i in range (0, length):
    element = int(input())
    vector.append(element)

for i in range (0, len(vector)):
    if prime_bool(vector[i]) == True:
        primes.append(vector[i])

if len(primes) == 0:
    print("There was no prime number found in the input list!")
else:
    print("There were found the following prime numbers:")
    print(primes)