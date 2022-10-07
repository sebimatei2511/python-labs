# Exercitiul 9
# Write a functions that determine the most common letter in a string. 
# For example if the string is "an apple is not a tomato", 
# then the most common character is "a" (4 times). 
# Only letters (A-Z or a-z) are to be considered. 
# Casing should not be considered "A" and "a" represent the same character.

def most_common_letter(string_input):
    dictionary = {}
    max_count = 0

    for i in string_input:
        if i in dictionary:
            dictionary[i] = dictionary[i] + 1
        else:
            dictionary[i] = 1
    
    for i in dictionary:
        if dictionary[i] > max_count:
            max_count = dictionary[i]
            the_letter = i
    
    return the_letter

print(most_common_letter(input()))
