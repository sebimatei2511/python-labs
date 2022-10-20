# Exercitiul 10
# Write a function that receives a variable number of lists and returns a list of tuples as follows: 
# the first tuple contains the first items in the lists, 
# the second element contains the items on the position 2 in the lists, etc. 
# Ex: for lists [1,2,3], [5,6,7], ["a", "b", "c"] 
# return: [(1, 5, "a ") ,(2, 6, "b"), (3,7, "c")]. 
# Note: If input lists do not have the same number of items, 
# missing items will be replaced with None to be able to generate max ([len(x) for x in input_lists]) tuples.

def the_function(no_of_lists):
    list_of_lists = []
    max_count = 0
    result_lists = []

    for i in range(0, no_of_lists):
        list_input = input("Add a list: ").split()
        list_of_lists.append(list_input)

    for i in list_of_lists:
        if len(i) > max_count:
            max_count = len(i)

    for i in list_of_lists:
        if len(i) < max_count:
            for index in range(0, max_count - len(i)):
                i.append("none")

    for j in range(0, max_count):
        new_list = []
        for i in range(0, no_of_lists):
            new_list.append(list_of_lists[i][j])
        result_lists.append(new_list)

    return result_lists

print(the_function(3))