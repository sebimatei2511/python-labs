# Exercitiul 2
# Write a function that receives a string as a parameter 
# and returns a dictionary in which the keys are 
# the characters in the character string and the values 
# are the number of occurrences of that character 
# in the given text.
# Example: For string "Ana has apples." given as a parameter 
# the function will return the dictionary: 
# {'a': 3, 's': 2, '.': 1, 'e': 1, 'h': 1, 'l': 1, 'p': 2, ' ': 2, 'A': 1, 'n': 1}

from calendar import c


def The_function(string_input):
    dictionary = {}
    result_list = []

    for character in string_input:
        if character in dictionary:
            dictionary[character] += 1
        else:
            dictionary[character] = 1

    for key in dictionary:
        result_list.append((key, dictionary[key]))

    print(result_list)

The_function("Ana has apples")