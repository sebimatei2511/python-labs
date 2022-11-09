# Exercitiul 7
# Write a function called process that receives a variable number of keyword arguments
# The function generates the first 1000 numbers of the Fibonacci sequence 
# and then processes them in the following way:
# If the function receives a parameter called filters, this will be a list of predicates 
# (function receiving an argument and returning True/False) and will retain 
# from the generated numbers only those for which the predicates are True. 
# If the function receives a parameter called limit, it will return only that amount of numbers from the sequence. 
# If the function receives a parameter called offset, 
# it will skip that number of entries from the beginning of the result list. 
# The function will return the processed numbers.
# Example:

# def sum_digits(x):
#     return sum(map(int, str(x)))

# process(
#     filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],
#     limit=2,
#     offset=2
# ) 
# returns [34, 144]

# Explanation:
# Fibonacci sequence will be: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610...
# Valid numbers are: 2, 8, 34, 144, 610, 2584, 10946, 832040
# After offset: 34, 144, 610, 2584, 10946, 832040
# After limit: 34, 144

def sum_digits(x):
    return sum(map(int, str(x)))

def the_function(**kwargs):
    fibonacci = []
    fibonacci.append(0)
    fibonacci.append(1)
    for index in range(2, 1000):
        fibonacci.append(fibonacci[index - 2] + fibonacci[index - 1])

    if 'filters' in kwargs.keys():
        fibonacci_new = []
        for number in fibonacci:
            checker = 0
            for predicate in kwargs['filters']:
                if predicate(number) == False:
                    checker = 1
            if checker == 0: 
                fibonacci_new.append(number)
    
    fibonacci = fibonacci_new
    fibonacci_new = []
    if 'offset' in kwargs.keys():
        fibonacci_new = fibonacci[kwargs['offset']:]

    fibonacci = fibonacci_new
    fibonacci_new = []
    if 'limit' in kwargs.keys():
        fibonacci_new = fibonacci[:kwargs['limit']]

    return fibonacci_new
        
print(the_function(filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20], limit=2, offset=2))