# Exercitiul 4
# Să se scrie o funcție ce returnează o listă cu extensiile unice 
# a fișierelor din directorul dat ca argument la linia de comandă (nerecursiv). 
# Lista trebuie să fie sortată crescător.

import os

def the_function(my_path):
    extens_dict = dict([])

    for index in os.listdir(my_path):
        if os.path.isfile(index):
            split_tup = os.path.splitext(index)
            if split_tup[1] not in extens_dict:
                extens_dict[split_tup[1]] = 1
            else:
                extens_dict[split_tup[1]] += 1

    result = {i for i in extens_dict if extens_dict[i] == 1}
    print(result)
    

the_function("D:\Documente facultate\Anul III\PP - Programare în Python\Lab 4")