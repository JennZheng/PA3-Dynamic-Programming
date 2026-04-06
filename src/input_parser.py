import sys

def input_parser(filename):
    if not filename:
        raise ValueError("Invalid filename")
    
    #read the lines
    with open(filename, "r") as f:
        lines = [line.strip() for line in f if line.strip()]
    
    if not lines:
        raise ValueError("Empty input file")
    
    k = int(lines[0])
    char_values = {}

    #read character-value pairs
    for i in range(1, k + 1):
        parts = lines[i].split()
        if len(parts) != 2:
            raise ValueError("Invalid Line")
        char, val = parts
        char_values[char] = int(val)
    
    #read two strings
    A = lines[k+1]
    B= lines[k+2]

    return char_values, A, B