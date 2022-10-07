# Exercitiul 3
# Write a script that receives two strings and prints 
# the number of occurrences of the first string in the second.

from itertools import count

def number_of_occurrences(substr,str):
    counter = 0
    start_point = 0

    while(start_point < len(str)):
        position = str.find(substr, start_point)
        if(position != -1):
            start_point = position + 1
            counter = counter + 1
        else:
            break
    return counter

sub_string = input()
big_string = input()

print("The number of occurrences of the first string in the second is: ", 
number_of_occurrences(sub_string,big_string))