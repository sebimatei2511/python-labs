# Exercitiul 3
# Using functions, anonymous functions, list comprehensions and filter, 
# implement three methods to generate a list with all the vowels in a given string.
# For the string "Programming in Python is fun" 
# the list returned will be ['o', 'a', 'i', 'i', 'o', 'i', 'u'].

# Method 1 - using list comprehensions and basic functions
def the_first(string_input):
    vowels = "aeiouAEIOU"
    result_list = []
    
    for character in string_input:
        if character in vowels:
            result_list.append(character)

    return result_list

print(the_first("Ana are mere"))



# Method 2 - using anonymous functions
vowels = "aeiouAEIOU"
the_second = lambda string_input : [character for character in string_input if character in vowels]

print(the_second("Ana are mere"))



# Method 3 - using filter
def the_third(string_input):
    vowels = "aeiouAEIOU"

    for character in string_input:
        if character in vowels:
            return True
        else:
            return False

filtered = filter(the_third, "Ana are mere")
print(list(filtered))
    