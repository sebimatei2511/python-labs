# Exercitiul 5
# The validate_dict function that receives as a parameter a set of tuples 
# ( that represents validation rules for a dictionary that has strings as keys and values) 
# and a dictionary. A rule is defined as follows: (key, "prefix", "middle", "suffix"). 
# A value is considered valid if it starts with "prefix", "middle" is inside the value 
# (not at the beginning or end) and ends with "suffix". The function will 
# return True if the given dictionary matches all the rules, False otherwise.

def apply_rule(rule, string):
    return (string.startswith(rule[1]) and string.find(rule[2]) and string.endswith(rule[3]))

def the_function(rules, strings):
    rules_status = True

    for key in strings:
        OK = False

        for tuplu in rules:
            if (tuplu[0] == key):
                OK = True
                rules_status = rules_status and apply_rule(tuplu, d[key])

        if OK == False: 
            return False
        
    return rules_status

s = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
d = {"key1": "come inside, it's too cold out", "key3": "this is invalid"}
print(the_function(s, d))
