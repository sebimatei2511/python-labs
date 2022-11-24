# Exercitiul 8
# Write a function that recursively scrolls a directory and 
# displays those files whose name matches a regular expression 
# given as a parameter or contains a string that matches the same expression. 
# Files that satisfy both conditions will be prefixed with ">>" 

import re
import os

def the_function(path, regex):
    result_list = []

    for root, directories, files in os.walk(path):
        for file in files:

            file_path = os.path.join(root, file)
            check_name = re.match(regex, file)
            contains_a_string = re.match(regex, open(file_path, "r").read())

            if check_name or contains_a_string:
                result_list.append(file_path)
            elif check_name and contains_a_string:
                result_list.append(">>" + file_path)

    return result_list

print(the_function("D:\Documente facultate\Anul III\PP - Programare în Python\Lab 6", r"\d"))
