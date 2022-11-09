# Exercitiul 5
# Write a function with one parameter which represents a list. 
# The function will return a new list containing all the numbers found in the given list.
# Example: my_function([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]) will return [1, 5, 6, 3.0]

def the_function(list_input):
    result_list = []

    for element in list_input:
        if type(element) == int or type(element) == float or type(element) == complex:
            result_list.append(element)

    return result_list

print(the_function([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))