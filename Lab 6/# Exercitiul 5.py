# Exercitiul 5
# Write another variant of the function from the previous exercise 
# that returns those elements that have at least one attribute 
# that corresponds to a key-value pair in the dictionary.

import xml.etree.ElementTree as ET

def the_function(path, attrs_dictionary):
    resut_list =[]

    tree = ET.parse(path)
    root = tree.getroot()

    for child in root:
        switch = False
        for key in attrs_dictionary:
            if child.attrib.get(key) == attrs_dictionary[key]:
                switch = True

        if switch == True:
            resut_list.append(child.tag)
        
    return resut_list

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
