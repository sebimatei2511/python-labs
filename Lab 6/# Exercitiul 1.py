# Exercitiul 1
# Write a function that extracts the words from a given text as a parameter. 
# A word is defined as a sequence of alpha-numeric characters.

import re

def the_function(string_input):
    result = re.findall(r'\w+', string_input)
    return result

print(the_function("Ana are mere si   pere! George nu mananca mere."))