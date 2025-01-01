def ascii_to_string(input_ascii_codes: list[int]) -> str:
    return ''.join(chr(value) for value in input_ascii_codes)
    
#''.join(...): This joins all the characters into a single string. The join() method takes a list of strings (or characters, in this case) and concatenates them into one string.    
#List comprehension: The list comprehension [chr(value) for value in ascii_values] loops through each ASCII value in the list and converts it to its corresponding character using chr().
#chr(value): This function takes an integer (representing an ASCII value) and returns the corresponding character. For example, chr(72) returns 'H', chr(101) returns 'e', and so on.
print(ascii_to_string([80, 114, 111, 103, 114, 97, 109, 109, 105, 110, 103, 32, 112, 117, 122, 122, 108, 101, 115, 33]))