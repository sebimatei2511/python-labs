# Exercitiul 7
# Write a function that receives as parameter a list of numbers (integers) 
# and will return a tuple with 2 elements. The first element of the tuple 
# will be the number of palindrome numbers found in the list 
# and the second element will be the greatest palindrome number.

def palindrome_bool(number_input):
    copy = number_input
    reverse_number = 0

    while number_input > 0:
        reverse_number = (reverse_number * 10) + (number_input % 10)
        number_input = number_input // 10

    if copy == reverse_number:
        return True
    else:
        return False

def the_function(list_of_numbers):
    number_of_palindromes = 0
    biggest_palindrome = 0

    for i in range(0, len(list_of_numbers)):
        if palindrome_bool(list_of_numbers[i]) == True:
            number_of_palindromes = number_of_palindromes + 1
            if list_of_numbers[i] > biggest_palindrome:
                biggest_palindrome = list_of_numbers[i]
    
    return number_of_palindromes, biggest_palindrome

print(the_function([121,1221,23,43,3]))