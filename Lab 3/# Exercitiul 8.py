# Exercitiul 8
# Write a function that receives a single dict parameter named mapping. 
# This dictionary always contains a string key "start". 
# Starting with the value of this key you must obtain a list of objects by iterating 
# over mapping in the following way: the value of the current key is the key for the next value, 
# until you find a loop (a key that was visited before). 
# The function must return the list of objects obtained as previously described.
# Ex: loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}) 
# will return ['a', '6', 'z', '2']

def loop(dict):
    key = 'start'
    result_list = []

    while dict[key] not in result_list:
        result_list.append(dict[key])
        key = dict[key]

    print(result_list)

loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'})
