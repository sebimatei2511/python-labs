# Exercitiul 4
# Write a function that receives as a parameters a list of musical notes (strings), 
# a list of moves (integers) and a start position (integer). 
# The function will return the song composed by going though the musical notes 
# beginning with the start position and following the moves given as parameter.
# Example : compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2) will return ["mi", "fa", "do", "sol", "re"] 

def the_function(musical_notes, list_of_moves, start_pos):
    result = []
    result.append(musical_notes[start_pos])

    for index in range(0, len(list_of_moves)):
        print(list_of_moves[index])
        start_pos = (start_pos + list_of_moves[index]) % len(musical_notes)
        result.append(musical_notes[start_pos])

    return result

musical_notes = ["do", "re", "mi", "fa", "sol"]
list_of_moves = [1, -3, 4, 2]
start_pos = 2

print(the_function(musical_notes, list_of_moves, start_pos))
