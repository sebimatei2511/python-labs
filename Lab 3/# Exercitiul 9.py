# Exercitiul 9
# Write a function that receives a variable number of positional arguments 
# and a variable number of keyword arguments adn will return the number 
# of positional arguments whose values can be found among keyword arguments values.
# Ex: my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5) will return returna 3

def the_function(*args, **kwargs):
    counter = 0
    for element in args:
        for arg in kwargs:
            if kwargs.get(arg) == element:
                counter = counter + 1

    print(counter)

the_function(1, 2, 3, 4, x=1, y=2, z=3, w=5)