# Exercitiul 2
# Write a script that calculates how many vowels are in a string.

def number_of_vowels(str):
    counter = 0
    vowel = "aeiouAEIOU"

    for letter in str:
        if letter in vowel:
            counter = counter + 1
    
    return counter

str = input()
print(str, " has ", number_of_vowels(str), " vowels.")