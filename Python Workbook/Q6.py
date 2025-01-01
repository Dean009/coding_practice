def filter_even_length_strings(input_strs: list[str]) -> list[str]:
    # Create a new list to store strings with an even number of characters
    newstringlist = []
    
    for str in input_strs:
        # Check if the length of the string is even
        if len(str) % 2 == 0:
            newstringlist.append(str)
    
    return newstringlist

    
print(filter_even_length_strings(["cat","dog","fish","elephant"]))