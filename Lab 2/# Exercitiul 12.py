# Exercitiul 12
# Write a function that will receive a list of words  as parameter and 
# will return a list of lists of words, grouped by rhyme. 
# Two words rhyme if both of them end with the same 2 letters.
# Example:
#   group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']) will return [['ana', 'banana'], ['carte', 'parte'], ['arme']] 

def the_function(list_input):
    result_list = []
    for i in range(0, len(list_input) - 1):

        if list_input[i] != "":

            short_list = []
            short_list.append(list_input[i])

            for j in range(i + 1, len(list_input)):
                if list_input[i] != "" and list_input[j] != "":
                    if (list_input[i][len(list_input[i]) - 1] == list_input[j][len(list_input[j]) - 1]) and ( list_input[i][len(list_input[i]) - 2] == list_input[j][len(list_input[j]) - 2] ):
                        
                        short_list.append(list_input[j])

                        list_input[j] = ""
            
            list_input[i] = ""

            if short_list != []:
                result_list.append(short_list)

    if list_input[len(list_input) - 1] != "":
        short_list = []
        short_list.append(list_input[len(list_input) - 1])
        result_list.append(short_list)
    
    return result_list

lista = ['ana', 'banana', 'carte', 'arme', 'parte']
print(the_function(lista))