# Exercitiul 3
# Să se scrie o funcție ce primește ca parametru un string my_path.
# Dacă parametrul reprezintă calea către un fișier, se vor returna ultimele 20 de caractere din conținutul fișierului. 
# Dacă parametrul reprezintă calea către un director, se va returna o listă de tuple (extensie, count), 
# sortată descrescător după count, unde extensie reprezintă extensie de fișier, iar count - numărul de fișiere cu acea extensie. 
# Lista se obține din toate fișierele (recursiv) din directorul dat ca parametru. 

import ntpath
import os
from collections import Counter

global result_list
result_list = []

global switch
switch = 0

def the_function(my_path):
    isFile = os.path.isfile(my_path)
    isDirectory = os.path.isdir(my_path)

    if isFile == True:
        if switch == 0:
            file_open = open(my_path, 'r')
            lines = file_open.read()
            print(lines[-20:])
            return
            
        else:
            split_tup = os.path.splitext(ntpath.basename(my_path))
            result_list.append(split_tup[1])

    elif isDirectory == True:
        switch = 1
        for index in os.listdir(my_path):      
            if os.path.isdir(index) == True:
                the_function(os.path.abspath(index))
            else:
                split_tup = os.path.splitext(index)
                if split_tup[1] != '':
                    result_list.append(split_tup[1])

    print(Counter(result_list))

the_function(r"D:\\Documente facultate\\Anul III\\PP - Programare în Python")
