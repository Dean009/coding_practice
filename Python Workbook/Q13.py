def filter_strings_with_vowels(input_strs: list[str]) -> list[str]:
    # Your implementation here
    return_string = []
    for c in input_strs:
        for word in c.split():
            if 'a' in word or 'e' in word or 'i' in word or 'o' in word or 'u' in word:
                return_string.append(word)
    return return_string    

print(filter_strings_with_vowels(["apple", "banana", "zyxvb"]))
print(filter_strings_with_vowels([]))
print(filter_strings_with_vowels(["q", "w", "e", "r", "t", "y"]))
