def censor_python(input_strs: list[str]) -> list[str]:
    return_list = []  # Initialize the list to store results
    letters_to_replace = {"P", "Y", "T", "H", "O", "N"}  # Letters to replace (case insensitive)
    
    for word in input_strs:
        new_word = ""  # Initialize a new word for each iteration
        for char in word:
            if char.upper() in letters_to_replace:  # Check if the character is in the set
                new_word += "X"  # Replace with "X"
            else:
                new_word += char  # Keep the original character
        return_list.append(new_word)  # Add the modified word to the result list
    
    return return_list  # Return the final list

# Example usage
print(censor_python(["python", "hello", "HELLO", "PYTHON", "example"]))