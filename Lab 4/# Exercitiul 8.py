# Exercitiul 8
# Să se scrie o funcție ce primește un parametru cu numele dir_path. 
# Acest parametru reprezintă calea către un director aflat pe disc. 
# Funcția va returna o listă cu toate căile absolute ale fișierelor aflate în rădăcina directorului dir_path.

import os

def the_function(dir_path):
    result_list = []
    for index in os.listdir(dir_path):
        if os.path.isfile(index) == True:
            result_list.append(os.path.abspath(index))

    print(result_list)

the_function("D:\Documente facultate\Anul III\PP - Programare în Python\Lab 3")