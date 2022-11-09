# Exercitiul 4
# Write a function that receives a variable number of arguments and keyword arguments. The function returns a list containing only the arguments which are dictionaries, containing minimum 2 keys and at least one string key with minimum 3 characters.
# Example:
# my_function(
# {1: 2, 3: 4, 5: 6}, 
# {'a': 5, 'b': 7, 'c': 'e'}, 
# {2: 3}, 
# [1, 2, 3],
# {'abc': 4, 'def': 5},
# 3764,
# dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},
# test={1: 1, 'test': True}
# ) 
# will return: [{'abc': 4, 'def': 5}, {1: 1, 'test': True}]

def the_function(*args, **kwargs):
    result_list = []

    for argument in args:
        if type(argument) == dict and len(argument.keys()) >= 2:
            find_out = False

            for key in argument.keys():
                if type(key) == str and len(key) >= 3:
                    find_out = True

            if find_out == True:
                result_list.append(argument)

    for argument in kwargs.keys():
        if type(kwargs[argument]) == dict and len(kwargs[argument].keys()) >= 2:
            find_out = False

            for key in kwargs[argument].keys():
                if type(key) == str and len(key) >= 3:
                    find_out = True

            if find_out == True:
                result_list.append(kwargs[argument])

    return result_list

print(the_function( {1: 2, 3: 4, 5: 6}, {'a': 5, 'b': 7, 'c': 'e'}, 
{2: 3}, [1, 2, 3], {'abc': 4, 'def': 5}, 3764, 
dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'}, test={1: 1, 'test': True}))