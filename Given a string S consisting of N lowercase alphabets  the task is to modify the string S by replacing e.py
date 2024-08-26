def modify_string(S):
    from collections import Counter
    frequency = Counter(S)
    modified_string = ""
    for char in S:
        circular_distance = frequency[char]
        new_char = chr((ord(char) - ord('a') + circular_distance) % 26 + ord('a'))
        modified_string += new_char
    return modified_string
S = "ghee"
output = modify_string(S)
print(output)  
