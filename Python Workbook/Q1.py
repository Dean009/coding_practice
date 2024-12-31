def filter_strings_containing_a(input_strs: list[str]) -> list[str]:
    output = []
    for input in input_strs:
        if "a" in input:  # Check if 'a' is in the string
            output.append(input)  # Add the string to the output list
    return output  # Return the filtered list

# Test the function
print(filter_strings_containing_a(["apple", "banana", "cherry", "date"]))


#-> list[str]:
#This is the return type. It tells you what type of data the function will return after it completes its task.

