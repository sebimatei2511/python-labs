# Exercitiul 3
# Write a function that receives as parameters two lists a and b 
# and returns: (a intersected with b, a reunited with b, a - b, b - a)

def the_function(a, b):
    m = len(a)
    n = len(b)
    a_intersected_b = []
    a_reunited_b = []
    
    for value in a:
        if value in b:
            a_intersected_b.append(value)

    print("The intersection is:")
    print(a_intersected_b)

    a_reunited_b = list(set(a) | set(b))
    print("The reunion is:")
    print(a_reunited_b)

    a_minus_b = list(set(a).difference(set(b)))
    print("A minus B:")
    print(a_minus_b)

    b_minus_a = list(set(b).difference(set(a)))
    print("B minus A:")
    print(b_minus_a)



a = [1,2,3,4,5,6,7,8,9,21]
b = [2,3,4,8,9,10,12,11,13,20,21]
the_function(a, b)