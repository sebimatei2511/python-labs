# Exercitiul 1
# Write a function that receives as 
# parameters two lists a and b and returns a list of sets containing: 
# (a intersected with b, a reunited with b, a - b, b - a)

def the_function(a, b):
    results_list = []
    a = set(a)
    b = set(b)

    a_intersected_b = set.intersection(a, b)
    results_list.append(a_intersected_b)
    a_reunited_b = (set(a) | set(b))
    results_list.append(a_reunited_b)
    a_minus_b = (set(a).difference(set(b)))
    results_list.append(a_minus_b)
    b_minus_a = (set(b).difference(set(a)))
    results_list.append(b_minus_a)

    print("The input lists are:")
    print(a)
    print(b)
    print("------------------------------")
    print("The intersections of the given lists is:", results_list[0])
    print("The reunion of the given lists is:", results_list[1])
    print("The difference between a and b is:", results_list[2])
    print("The difference between b and a is:", results_list[3])

a = [1,2,3,4,5,6,7,8,9,21]
b = [2,3,4,8,9,10,12,11,13,20,21]
the_function(a, b)