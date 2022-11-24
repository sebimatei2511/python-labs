# Exercitiul 6
# Write a function that, for a text given as a parameter, 
# censures words that begin and end with vowels. 
# Censorship means replacing characters from odd positions with *.

import re

def the_function(string_input):
    words_to_edit = re.findall('[aeiouAEIOU]\w*[aeiouAEIOU]', string_input)
    words_list = re.findall(r'\w+', string_input)
    result_string = ""
    count = 0
    var_string = ""

    for word in words_list:
        count += 1

        if word in words_to_edit:
            for index in range(1, len(word) + 1):
                
                if index % 2 == 0:
                    var_string = var_string + word[index - 1]
                else:
                    var_string = var_string + '*'
         
        if var_string == "":
            result_string = result_string + word
        else:
            result_string = result_string + var_string
        var_string = ""

        if count != len(words_list):
            result_string = result_string + " "

    return result_string

print(the_function("Astazi este ziua numarul Opatru din saptamana"))
