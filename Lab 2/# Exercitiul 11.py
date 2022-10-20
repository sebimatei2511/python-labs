# Exercitiul 11
# Write a function that will order a list of string tuples based on the 3rd character of the 2nd element in the tuple. 
# Example: ('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]

def order_2_tuples(tuple1, tuple2):

    return tuple2, tuple1

def the_function(list_of_tuples):

    for i in range(0, len(list_of_tuples) - 1):
        for j in range(i + 1, len(list_of_tuples)):
            first_second_element = list_of_tuples[i][1]
            second_second_element = list_of_tuples[j][1]

            if first_second_element[2] > second_second_element[2]:
                aux = list_of_tuples[i]
                list_of_tuples[i] = list_of_tuples[j]
                list_of_tuples[j] = aux
    
    return list_of_tuples

list_of_tuples = [('abc', 'bcd'), ('abc', 'zzb'),('abc', 'cca')]
print(the_function(list_of_tuples))