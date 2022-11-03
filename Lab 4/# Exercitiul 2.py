# Exercitiul 2
# Să se scrie o funcție ce primește ca argumente două căi: director si fișier. 
# Implementati functia astfel încât în fișierul de la calea fișier să fie scrisă pe câte o linie, 
# calea absolută a fiecărui fișier din interiorul directorului de la calea folder, ce incepe cu litera A.

import os

def the_function(directory, file_input):
    file_input = open("text_file.txt", "w+")

    for index in os.listdir(directory):
        split_tup = os.path.splitext(index)
        name_of_file = split_tup[0]
        
        if name_of_file[0] == 'A':
            path_abs = os.path.abspath(index)
            file_input.write(path_abs)
            file_input.write("\n")

    file_input.close()

the_function(r"C:\Users\sebim\Downloads", "D:\Documente facultate\Anul III\PP - Programare în Python\Lab 4\text_file.txt")