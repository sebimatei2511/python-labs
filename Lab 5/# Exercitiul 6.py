# Exercitiul 6
# Write a function that receives a list with integers as parameter that contains 
# an equal number of even and odd numbers that are in no specific order. 
# The function should return a list of pairs (tuples of 2 elements) of 
# numbers (Xi, Yi) such that Xi is the i-th even number in the list and Yi is the i-th odd number
# Example:
# my_function([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]) will return [(2, 1), (8, 3), (4, 5), (10, 7), (2, 9)]

def the_function(input_list):
    even_list = []
    odd_list = []
    result_list = []

    for element in input_list:
        if element % 2 == 0:
            even_list.append(element)
        else:
            odd_list.append(element)

    for index in range(0, len(input_list)//2):
        result_list.append((even_list[index], odd_list[index]))

    return result_list

print(the_function([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))