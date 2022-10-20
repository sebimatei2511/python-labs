# Exercitiul 6
# Write a function that receives as a parameter a variable number of lists 
# and a whole number x. Return a list containing the items 
# that appear exactly x times in the incoming lists. 
# Example: For the [1,2,3], [2,3,4],[4,5,6], [4,1, "test"] 
# and x = 2 lists [1,2,3 ] # 1 is in list 1 and 4, 
# 2 is in list 1 and 2, 3 is in lists 1 and 2.

import collections

def the_function(no_of_lists, x):
    list_of_lists = []
    result_list = []

    for index in range(0, no_of_lists):
        list_input = input("Add a list: ").split()
        list_of_lists = list_of_lists + list_input

    freq = collections.Counter(list_of_lists)

    for key, value in freq.items():
        if value == x:
            result_list.append(key)

    return result_list

x = int(input("Enter a whole number:"))
y = int(input("Enter a number of lists:"))
print(the_function(y,x))
