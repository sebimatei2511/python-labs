# Exercitiul 2
# Create a function and an anonymous function that receive a variable number of arguments. 
# Both will return the sum of the values of the keyword arguments.
# Example:
# For the call my_function(1, 2, c=3, d=4) the returned value will be 7.

def the_function(*args, **kwargs):
    sum_result = 0

    for argument in kwargs.keys():
        sum_result = sum_result + kwargs[argument]

    for argument in args:
        sum_result = sum_result + argument

    return sum_result

the_anonymous_function = lambda *args, **kwargs: sum(args) + sum(kwargs.values())

print(the_function(1, 2, c=3, d=4, e=5))
print(the_anonymous_function(1, 2, 3, a=4, b=5))
