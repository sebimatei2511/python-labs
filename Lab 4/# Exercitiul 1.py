# Exercitiul 1
# Să se scrie o funcție ce primeste un singur parametru, director, ce reprezintă calea către un director. 
# Funcția returnează o listă cu extensiile unice sortate crescator (in ordine alfabetica) a fișierelor din directorul dat ca parametru.
# Mențiune: extensia fișierului ‘fisier.txt’ este ‘txt’ 

import os

def the_function(directory):
    result_list = []

    for index in os.listdir(directory):
        split_tup = os.path.splitext(index)
        result_list.append(split_tup[1])

    print(result_list)

the_function("D:\Documente facultate\Anul III\PP - Programare în Python\Lab 3")