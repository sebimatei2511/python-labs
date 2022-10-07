# Exercitiul 4
# Write a script that converts a 
# string of characters written in UpperCamelCase into lowercase_with_underscores.

def change_way(string_input):
    result = [string_input[0].lower()]
    uppers = 'QWERTYUIOPASDFGHJKLZXCVBNM'

    for letter in string_input[1:]:
        if letter in uppers:
            result.append('_')
            result.append(letter.lower())
        else:
            result.append(letter)
    
    return ''.join(result)

string_input = input()
print( string_input, " becomes ", change_way(string_input))