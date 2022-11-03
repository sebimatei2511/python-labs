# Exercitiul 7
# Să se scrie o funcție care primește ca parametru un șir de caractere care reprezintă 
# calea către un fișer si returnează un dicționar cu următoarele cămpuri: 
# full_path = calea absoluta catre fisier, file_size = dimensiunea fisierului in octeti, 
# file_extension = extensia fisierului (daca are) sau "", can_read, 
# can_write = True/False daca se poate citi din/scrie in fisier.

import os

def the_function(my_path):
    dictionar = dict([])

    dictionar["full_path"] = os.path.abspath(my_path)
    dictionar["file_size"] = os.path.getsize(my_path)

    split_tup = os.path.splitext(my_path)
    dictionar["file_extension"] = split_tup[1]

    dictionar["can_read"] = os.access(my_path, os.W_OK)
    dictionar["can_write"] = os.access(my_path, os.R_OK)

    return dictionar

print(the_function(r"D:\Documente facultate\Anul III\PP - Programare în Python\Lab 4\text_file.txt"))