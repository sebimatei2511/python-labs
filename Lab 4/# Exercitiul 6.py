# Exercitiul 6
# Să se scrie o funcție care are același comportament ca funcția de la exercițiul anterior, 
# cu diferența că primește un parametru în plus: o funcție callback, 
# care primește un parametru, iar pentru fiecare eroare apărută în procesarea fișierelor, 
# se va apela funcția respectivă cu instanța excepției ca parametru.

import os
from pathlib import Path

def the_function(target, callback: callable(Path)):

    if os.path.isfile(target):
        data_file = open(target, "r")
        lines = data_file.readlines()
        data_file.close()

        found = False
        for line in lines:
            if callback in line:
                found = True

        return found

    elif os.path.isdir(target):
        result_list = []

        for file in os.listdir(target):
            try:
                if os.path.isdir(file) == True:
                    result_list.append(the_function(file, callback))

                elif os.path.isfile(file) == True:
                    data_file = open(file, "r")
                    lines = data_file.readlines()
                    data_file.close()

                    found2 = False
                    for line in lines:
                        if callback in line:
                            found2 = True

                    if found2 == True:
                        result_list.append(file)
            except Exception as e:
                callback(e)

        if result_list == []:
            return False
        else:
            return result_list
    
    else:
        raise ValueError(target)

print(the_function("D:\Documente facultate\Anul III\PP - Programare în Python", "the_function"))