def count_special_characters(statement):
    special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
    count = sum(1 for char in statement if char in special_characters)
    return count
given_statement = "Modi Birthday @ September 17, #&$% is the wishes code for him."
result = count_special_characters(given_statement)
print(f"Number of special Characters: {result}")
