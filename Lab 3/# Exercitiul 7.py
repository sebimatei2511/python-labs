# Exercitiul 7
# Write a function that receives a variable number of sets and returns a dictionary with 
# the following operations from all sets two by two: reunion, intersection, a-b, b-a. 
# The key will have the following form: "a op b", where a and b are two sets, 
# and op is the applied operator: |, &, -. 

# Ex: {1,2}, {2, 3} =>
# {
#    "{1, 2} | {2, 3}":  {1, 2, 3},
#    "{1, 2} & {2, 3}":  { 2 },
#    "{1, 2} - {2, 3}":  { 1 },
#    ...
# }

def the_function(no_of_sets):
    list_of_sets = []
    dictionary = {}

    for i in range(0, no_of_sets):
        input_set = set(input("Please write a set: ").split())
        list_of_sets.append(input_set)
    
    for i in range(0, no_of_sets - 1):
        for j in range(i + 1, no_of_sets):
            set_reunion = list(list_of_sets[i] | list_of_sets[j])
            set_intersect = [value for value in list_of_sets[i] if value in list_of_sets[j]]
            set_a_minus_b = list(list_of_sets[i].difference(list_of_sets[j]))
            set_b_minus_a = list(list_of_sets[j].difference(list_of_sets[i]))

            dictionary[str(list_of_sets[i]) + " | " + str(list_of_sets[j])] = set(set_reunion)
            dictionary[str(list_of_sets[i]) + " & " + str(list_of_sets[j])] = set(set_intersect)
            dictionary[str(list_of_sets[i]) + " - " + str(list_of_sets[j])] = set(set_a_minus_b)
            dictionary[str(list_of_sets[j]) + " - " + str(list_of_sets[i])] = set(set_b_minus_a)

    print(dictionary)

            
the_function(4)
