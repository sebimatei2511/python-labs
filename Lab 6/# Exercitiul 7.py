# Exercitiul 7
# Verify using a regular expression whether a string is a valid CNP.

import re

# Am folosit structura unui CNP conform wikipedia
# CNP = SAALLZZJJNNNC, unde
# S = [1...8]
# AA = ultimele 2 cifre din anul nasterii
# LL = luna nasterii, cu valori intre 01 si 12
# ZZ = ziua nasterii, cu valori intre 01 si 31, dupa caz
# JJ = codul judetului, cu valori intre 01 si 52, dupa caz, in afara de 47-50 (desfiintate)
# NNN = numar secvential, cu valori intre 001 si 999
# C = cifra de control, calculata dupa un algoritm specific

def control_digit(string_input):
    # Pasii algoritmului sunt preluati de pe wikipedia, in functie de regulile prin care se creeaza cifra de control
    constanta_wiki = "279146358279"
    control_digit = 0

    for i, j in zip(constanta_wiki, string_input):
        control_digit = control_digit + (int(i) * int(j))
    
    control_digit = control_digit % 11

    if control_digit == 10:
        control_digit = 1

    return str(control_digit)

def how_many_days_in_a_month(year, month):
    # Creez un array in care sa stochez numarul de zile pentru fiecare luna
    array = [
        "(0[1-9]|[1-2]\d|3[0-1])", #january
        "(0[1-9]|1\d|2[0-8])",     #february
        "(0[1-9]|[1-2]\d|3[0-1])", #march
        "(0[1-9]|[1-2]\d|30)",     #april
        "(0[1-9]|[1-2]\d|3[0-1])", #may
        "(0[1-9]|[1-2]\d|30)",     #june
        "(0[1-9]|[1-2]\d|3[0-1])", #july
        "(0[1-9]|[1-2]\d|3[0-1])", #august
        "(0[1-9]|[1-2]\d|30)",     #september
        "(0[1-9]|[1-2]\d|3[0-1])", #october
        "(0[1-9]|[1-2]\d|30)",     #november
        "(0[1-9]|[1-2]\d|3[0-1])", #december
    ]

    # Tratez separat si cazul anului bisect
    if int(year) % 4 == 0:
        array[1] = "(0[1-9]|1\d|2[0-9])"

    return array[int(month) - 1]

def the_function(string_input):
    input_month = string_input[1:3]
    input_year = string_input[3:5]

    value_S = "[1-8]"
    value_AA = "\d{2}"
    value_LL = "(0[1-9]|1[0-2])"
    value_ZZ = how_many_days_in_a_month(input_month, input_year)
    value_JJ = "(0[1-9]|1[0-9]|2[0-9]|3[0-9]|4[0-6]|5[1-2])"
    value_NNN = "(\d\d\d)"
    value_C = control_digit(string_input[:-1])

    cnp_builder = "^" + value_S + value_AA + value_LL + value_ZZ + value_JJ + value_NNN + value_C + r"$"

    print(cnp_builder)
    if re.match(cnp_builder, string_input):
        print("CNP corect :)")
    else:
        print("CNP-ul nu este valid!!!")

the_function("5001125123456")
