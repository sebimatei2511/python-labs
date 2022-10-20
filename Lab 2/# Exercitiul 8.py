# Exercitiul 8
# Write a function that receives a number x, default value equal to 1, a list of strings, and a boolean flag set to True. 
# For each string, generate a list containing the characters that have the ASCII code divisible 
# by x if the flag is set to True, otherwise it should contain characters that have the ASCII code not divisible by x.
# Example: x = 2, ["test", "hello", "lab002"], flag = False 
# will return (["e", "s"], ["e" . Note: The function must return list of lists.

def the_function(list_of_string, x = 1, flag = True):
    result_list = []

    for string_input in list_of_string:
        new_list = []

        if flag == True:
            for index in string_input:
                if ord(index) % x == 0:
                    new_list.append(index)

        elif flag == False:
            for index in string_input:
                if ord(index) % x != 0:
                    new_list.append(index)

        result_list.append(new_list)
    
    return result_list

print(the_function(["test", "hello", "lab002"], 2, False))
print(the_function(["test", "hello", "lab002"]))
