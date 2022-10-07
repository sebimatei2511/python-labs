# Exercitiul 10
# Write a function that counts how many words exists in a text. 
# A text is considered to be form out of words that are separated by only ONE space. 
# For example: "I have Python exam" has 4 words.

def number_of_words(string_input):

    the_number = 1

    for i in string_input:
        if i == " ":
            the_number = the_number + 1

    return the_number

print("Your input has ", number_of_words(input())," words.")