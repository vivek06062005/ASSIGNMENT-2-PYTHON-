def find_repeated_letters(word):
    letter_count = {}
    for letter in word:
        letter_count[letter] = letter_count.get(letter, 0) + 1    
    repeated_letters = {letter: count for letter, count in letter_count.items() if count > 1} 
    print(f"Number of repeated letters = {len(repeated_letters)}")
    if repeated_letters:
        print("Repeated letters =", ', '.join(repeated_letters.keys()))
word = input("Enter the word: ")
find_repeated_letters(word)
def are_isomorphic(s, t):
    if len(s) != len(t):
        return False   
    mapping_s_to_t = {}
    mapping_t_to_s = {}  
    for char_s, char_t in zip(s, t):
        if char_s in mapping_s_to_t:
            if mapping_s_to_t[char_s] != char_t:
                return False
        else:
            mapping_s_to_t[char_s] = char_t
        
        if char_t in mapping_t_to_s:
            if mapping_t_to_s[char_t] != char_s:
                return False
        else:
            mapping_t_to_s[char_t] = char_s           
    return True
s = "egg"
t = "add"
print(are_isomorphic(s, t))
