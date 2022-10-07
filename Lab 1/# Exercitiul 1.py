# Exercitiul 1
# Find The greatest common divisor of multiple numbers read from the console.

# Definim functie pentru gcd
def GCD(a,b):
    if(a==b):
        return a
    while(a!=b):
        if(a>b):
            a = a - b
        else:
            b = b - a
    return a

# Declaram un array in care sa retinem numerele
# si luam din consola dimensiunea array-ului
numbers_array = list()
array_lenght = int(input("The lenght of the list will be: "))

# Citim separat primul numar din array, in el vom pastra 
# rezultatul gcd
first_number = int(input())
numbers_array.append(first_number)

# Citim restul numerelor 
for i in range(0,array_lenght-1):
    number = int(input())
    first_number = GCD(first_number,number)
    numbers_array.append(number)

# Afisam rezultatul
print("Your input list was: ", numbers_array)
print("And the greatest common divisor is: ", first_number)


