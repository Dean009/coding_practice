def remove_vowels(input_str: str) -> str:
    return_string = ""
    for c in input_str:
        if c not in "aeiouAEIOU":
            return_string += c
    return return_string     
            
print (remove_vowels("hello world!"))