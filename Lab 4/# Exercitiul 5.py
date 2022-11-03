# Exercitiul 5
# Să se scrie o funcție care primește ca argumente două șiruri 
# de caractere, target și to_search și returneaza o listă de 
# fișiere care conțin to_search. Fișierele se vor căuta astfel: 4
# dacă target este un fișier, se caută doar in fișierul 
# respectiv iar dacă este un director se va căuta recursiv 
# in toate fișierele din acel director.
#  Dacă target nu este nici fișier, nici director, se va 
# arunca o excepție de tipul ValueError cu un mesaj 
# corespunzator.

import os

def the_function(target, to_search):
    result_list = []

    if os.path.isfile(target):
        data_file = open(target, "r")
        lines = data_file.readlines()
        data_file.close()

        found = False
        for line in lines:
            if to_search in line:
                found = True

        return found

    elif os.path.isdir(target):
        result_list = []

        for file in os.listdir(target):
            if os.path.isdir(file) == True:
                result_list.append(the_function(file, to_search))

            elif os.path.isfile(file) == True:
                data_file = open(file, "r")
                lines = data_file.readlines()
                data_file.close()

                found2 = False
                for line in lines:
                    if to_search in line:
                        found2 = True

                if found2 == True:
                    result_list.append(file)

        if result_list == []:
            return False
        else:
            return result_list
    
    else:
        raise ValueError(target)

print(the_function("D:\Documente facultate\Anul III\PP - Programare în Python", "the_function"))