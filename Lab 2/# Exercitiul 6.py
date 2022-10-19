# Exercitiul 6
# Write a function that receives as a parameter a variable number of lists 
# and a whole number x. Return a list containing the items 
# that appear exactly x times in the incoming lists. 
# Example: For the [1,2,3], [2,3,4],[4,5,6], [4,1, "test"] 
# and x = 2 lists [1,2,3 ] # 1 is in list 1 and 4, 
# 2 is in list 1 and 2, 3 is in lists 1 and 2.

#  A LOT OF PROBLEMS

import numpy as np
from operator import itemgetter

from sympy import re

def the_function(no_of_lists, x):
    reunion = []
    freq = []

    for index in range(0, no_of_lists):
        list_input = input("Add a list: ").split()
        reunion.append(list_input)

    reunion = map(itemgetter, reunion)

    for i in range(0, len(reunion)):
        print(reunion[i])

    return print(reunion)


the_function(4,2)
