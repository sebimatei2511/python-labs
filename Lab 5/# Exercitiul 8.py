# Exercitiul 8 a)
# Write a function called print_arguments with one parameter named function. 
# The function will return one new function which prints the arguments and the 
# keyword arguments received and will return the output of the function receives as a parameter.
# Example:
# def multiply_by_two(x):
#     return x * 2
# def add_numbers(a, b):
#     return a + b
# augmented_multiply_by_two = print_arguments(multiply_by_two)
# x = augmented_multiply_by_two(10)  # this will print: Arguments are: (10,), {} and will return 20.
# augmented_add_numbers = print_arguments(add_numbers)
# x = augmented_add_numbers(3, 4)  # this will print: Arguments are: (3, 4), {} and will return 7.

def multiply_by_two(x):
    return x * 2

def add_numbers(a, b):
    return a + b

def print_arguments(function):
    def new_function(*args, **kwargs):
        print("Arguments are: ", *args, **kwargs)
        return function(*args, **kwargs)
    
    return new_function

print("a)--------------------------------------------------------")
augmented_multiply_by_two = print_arguments(multiply_by_two)
x = augmented_multiply_by_two(10)
print(x)
print("----------------------------------------------------------")
augmented_add_numbers = print_arguments(add_numbers)
x = augmented_add_numbers(3, 4)
print(x)




# Exercitiul 8 b)
# Write a function called multiply_output with one parameter named function. 
# The function will return one new function which returns the 
# output of the function received multiplied by 2.
# Example:
# def multiply_by_three(x):
#     return x * 3
# augmented_multiply_by_three = multiply_output(multiply_by_three)
# x = augmented_multiply_by_three(10)  # this will return 2 * (10 * 3)

def multiply_by_three(x):
    return x * 3

def multiply_output(function):
    def new_function(*args, **kwargs):
        return function(*args, **kwargs) * 2
    
    return new_function

print("b)--------------------------------------------------------")
augmented_multiply_by_three = multiply_output(multiply_by_three)
x = augmented_multiply_by_three(10)
print(x)



# Exercitiul 8 c)
# Write a function called augment_function with two parameters named function and decorators. 
# decorators will be a list of functions which will have the same signature as the previous functions 
# (print_arguments, multiply_output). augment_function will create a new function which 
# is augmented using all the functions in the decorators list.
# Example:
# def add_numbers(a, b):
#     return a + b
# decorated_function = augment_function(add_numbers, [print_arguments, multiply_output]) 
# x = decorated_function(3, 4)  # this will print: Arguments are: (3, 4), {} and will return (2 * (3 + 4))

def add_numbers(a, b):
    return a + b

def augment_function(function, decorators):
    def new_function(*args, **kwargs):
        output = function(*args, **kwargs)

        for decorator in decorators:
            output = decorator(output)
        
        return output(*args, **kwargs)

    return new_function

print("c)--------------------------------------------------------")
decorated_function = augment_function(add_numbers, [print_arguments, multiply_output]) 
x = decorated_function(3, 4)
print(x)