# Exercitiul 8
# Write a function that counts how many bits with value 1 a number has. 
# For example for number 24, the binary format is 00011000, 
# meaning 2 bits with value "1"

number = int(input())
result = 0

while number > 0:
    rest = number % 2
    result = result + rest
    number = number // 2

print(result)
