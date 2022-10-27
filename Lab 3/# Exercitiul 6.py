# Exercitiul 6
# Write a function that receives as a parameter a list and returns a tuple (a, b), 
# representing the number of unique elements in the list, and b representing the number 
# of duplicate elements in the list (use sets to achieve this objective).

def the_function(input_list):
    count_uniques = 0
    count_duplicates = 0
    difference = input_list
    input_set = set(input_list)
    
    for element in input_set:
        if element in input_list:
            difference.remove(element)

    difference = set(difference)

    count_duplicates = len(difference)
    count_uniques = len(input_set) - count_duplicates
    
    print((count_duplicates, count_uniques))

the_function([1,2,2,2,3,3,4,5,2])