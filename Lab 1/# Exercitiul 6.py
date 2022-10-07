# Exercitiul 6
# Write a function that validates if a number is a palindrome.

def reverse_builder(number):

    reverse = 0
    number = int(number)
    while number > 0:
        last_digit = number % 10
        reverse = reverse * 10
        reverse = reverse + last_digit
        number = number // 10

    return reverse

def palindrome_check(number):

    if int(number) == reverse_builder(number):
        return True
    return False

number = input()
print("Is ", number, " a palindrome?")
print(palindrome_check(number))