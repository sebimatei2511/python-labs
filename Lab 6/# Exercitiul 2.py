# Exercitiul 2
# Write a function that receives as a parameter a regex string, 
# a text string and a whole number x, and returns those 
# long-length x substrings that match the regular expression.

import re

def the_function(regex_string, text_string, x):
    array = re.findall(regex_string, text_string)
    result_list = []

    for i in range(0, len(array)): 
        if len(array[i]) == x:
            result_list.append(array[i])

    return result_list

print(the_function('\w+', "Ana are mere si   pere! George nu mananca mere.", 4))