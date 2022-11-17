# Exercitiul 7
# Verify using a regular expression whether a string is a valid CNP.

import re

def the_function(cnp_input):
    regex_20 = "[12] [0-9] [0-9] (0[1-9] | 1[0-2]) (0[1-9] | 1[0-9] | 2[0-9] | 3[0-1]) (1[0-9] | 2[0-9] | 3[0-9] | 4[0-6] | 5[12]) \d{4}$"
    regex_21 = "[56] (0[0-9] | 1[0-9] | 2[0-2]) (0[1-9] | 1[0-2]) (0[1-9] | 1[0-9] | 2[0-9] | 3[0-1]) (1[0-9] | 2[0-9] | 3[0-9] | 4[0-6] | 5[12]) \d{4}$"
    if (re.match(regex_21, cnp_input) != None) or (re.match(regex_20, cnp_input) != None) :
        return True
    else:
        return False

print(the_function("5001125221234"))
# am incercat sa validez cat mai real, nu prea am reusit 
# am pus spatiile in regex doar pentru a putea fi urmarite mai bine secventele
