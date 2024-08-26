def find_character_in_string(input_string, character):
    index = -1
    for i in range(len(input_string)):
        if input_string[i] == character:
            index = i
            break
    return index
input_string = input("Enter the string: ")
character = input("Enter the character to be searched: ")
index = find_character_in_string(input_string, character)
if index != -1:
    print(f"{character} is found in string at index: {index}")
else:
    print(f"{character} is not found in the string.")
