# Exercitiul 7
# Write a function that extract a number from a text 
# (for example if the text is "An apple is 123 USD", 
# this function will return 123, or if the text is "abc123abc" 
# the function will extract 123). The function will extract 
# only the first number that is found.

def find_first_number(string):
    empty_string = ""

    for i in string:
        if i.isdigit():
            empty_string = empty_string + i
        else:
            if empty_string != "":
                break

    return empty_string

print(find_first_number("abc123abcabc123abcabc123abc"))
