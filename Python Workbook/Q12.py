#define a function that when called returns a list containing the ASCII numeric codes of each character of the string

def string_to_ascii(input_str: str) -> list[int]:
        return [ord(char) for char in input_str]
    #ord(char) converts a single character (char) to its ASCII value (or Unicode code point if it's a non-ASCII character).
    #The expression [ ... for char in input_str] is a list comprehension, which is a concise way to create a list in Python.
    
print(string_to_ascii("aA"))