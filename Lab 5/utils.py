# Exercitiul 1 a)

def prime_number(x):
    if x == 1:
        return True
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for div in range(3, x//2, 2):
        if x % div == 0:
            return False
    return True

def process_item(x):
    found = 0

    while found == 0:
        x = x + 1
        if prime_number(x) == True:
            found = 1
    
    return x
