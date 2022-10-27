# Exercitiul 3
# Compare two dictionaries without using the operator "==" returning True or False. 
# (Attention, dictionaries must be recursively covered because 
# they can contain other containers, such as dictionaries, lists, sets, etc.)

def compare_dicts(dict1, dict2):
    
    if len(dict1) != len(dict2):
        print("The input dictionaries are not equal!")
    else:
        flag = 0
        for i in dict1:
            if type(dict1.get(i)) != type(dict2.get(i)):
                flag = 1
                break
            elif dict1.get(i) != dict2.get(i):
                flag = 1
                break
    
    if flag == 0:
        print("The input dictionaries are equal!")
    else:
        print("The input dictionaries are not equal!")

dict1 = {"a": [2, 4], "b": 2}
dict2 = {"a": [2, 4], "b": 2}

compare_dicts(dict1, dict2)