def count_vowels_and_consonants(statement):
    vowels = "aeiouAEIOU"
    num_vowels = sum(1 for char in statement if char in vowels)
    num_consonants = sum(1 for char in statement if char.isalpha() and char not in vowels)
    print(f"Number of vowels = {num_vowels} Number of Consonants = {num_consonants}") 
    if num_vowels > num_consonants:
        print("Vowels are maximum.")
    elif num_consonants > num_vowels:
        print("Consonants are maximum.")
    else:
        print("Both are equal.")
input_statement = "Saveetha School of Engineering Sample"
count_vowels_and_consonants(input_statement)
