# Exercitiul 4
# The build_xml_element function receives the following 
# parameters: tag, content, and key-value elements given 
# as name-parameters. Build and return a string that 
# represents the corresponding XML element. 
# Example: build_xml_element ("a", "Hello there", 
# href =" http://python.org ", _class =" my-link ", 
# id= " someid ") returns  the string = 
# "<a href=\"http://python.org \ "_class = \" my-link \ "id = \" someid \ "> Hello there </a>"


def the_function(tag, content, **args):
    result_string = f'<{tag} '

    for key, value in args.items():
        result_string += f'{key}=\\\"{value}\\\"'

    result_string += f'>{content} </{tag}>'
    
    print(result_string)

the_function("a", "Hello there", href = "http://python.org", _class = "my-link", id = "someid")