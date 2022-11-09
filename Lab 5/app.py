# Exercitiul 1 b)

import utils 

loop = True
while loop:
    user_input = input("Please write a number as input:")
    if user_input == 'q':
        print("Stopping the program...")
        break
    else:
        print(utils.process_item(int(user_input)))