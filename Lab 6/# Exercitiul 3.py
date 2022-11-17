# Exercitiul 3
# Write a function that receives as a parameter a string of text 
# characters and a list of regular expressions and returns 
# a list of strings that match on at least one regular expression given as a parameter.

import re

def the_function(text_string, regex_list):
    result_list = []

    for text in text_string:
        for regex in regex_list:
            if re.match(regex, text):
                result_list.append(text)
                break

    return result_list

print(the_function(["alabama", "p0rt0c4l4", "1991225171234", "192.168.0.1"], ["[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", "[12]\d{12}"]))