# Exercitiul 4
# The build_xml_element function receives the following 
# parameters: tag, content, and key-value elements given 
# as name-parameters. Build and return a string that 
# represents the corresponding XML element. 
# Example: build_xml_element ("a", "Hello there", 
# href =" http://python.org ", _class =" my-link ", 
# id= " someid ") returns  the string = 
# "<a href=\"http://python.org \ "_class = \" my-link \ "id = \" someid \ "> Hello there </a>"

def the_function(tag, content, _href, _class, _id):
    result_string = ""

    result_string += "<"
    result_string += tag
    result_string += " href=\""
    result_string += _href
    result_string += "\" "
    result_string += "_class=\""
    result_string += _class
    result_string += "\" "
    result_string += " id=\""
    result_string += _id
    result_string += "\" >"
    result_string += content
    result_string += "</"
    result_string += tag
    result_string += ">"
    
    print(result_string)

the_function("a", "Hello there", "http://python.org", "my-link", "someid")