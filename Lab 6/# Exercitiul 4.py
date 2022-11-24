# Exercitiul 4
# Write a function that receives as a parameter the path to 
# an xml document and an attrs dictionary and returns those elements 
# that have as attributes all the keys in the dictionary and values ​​the corresponding values. 
# For example, if attrs={"class": "url", "name": "url-form", "data-id": "item"} 
# the items selected will be those tags whose attributes are class="url" 
# si name="url-form" si data-id="item".

import re

def the_function(path, attrs_dictionary):
    result_list = []

    with open(path, 'r') as file_data:
        data = file_data.read()
        pattern_string = r"<(\w+)"

        for key, value in attrs_dictionary.items():
            pattern_string += r"".join(" {key}=\"{value}\"".format(key=key, value=value))
        
        pattern_string = pattern_string + r">[^</\2>]*</\2>)"
        
        for i in re.findall(pattern_string, data):
            result_list.append(i[0])
    
    return result_list

print(the_function("test.xml", {"class": "url", "name": "url-form", "data-id": "item"}))

# test.xml contine liniile:

# <ab class="url" name="url-form" data-id="item"> ab
#     <abc class="url" name="url-form" data-id="ite1m">abc</abc>
#     <abcd class="url" name="url-form" data-id="item">abcd</abcd>
#     <abcde class="url" name="urlform" data-id="item">acbde</abcde>
#     <abcdef class="url" name="url-form" data-id="Item">abcdef</abcdef>
#     <abcdefg class="url" name="url-form" data-id="item">abcdefg</abcdefg>
#     <item>
#         <name>Nume</name>
#     </item>
# </ab>
