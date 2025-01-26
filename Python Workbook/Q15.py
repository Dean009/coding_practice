def filter_palindromes(input_strs: list[str]) -> list[str]:
    string_return = []
    for i in input_strs:
        if i[0] == i[-1]:
            string_return.append(i)
    return string_return
            
            
    
    
print (filter_palindromes(["cat","dog","racecar","deified","giraffe"]))
print (filter_palindromes(["kayak","giraffe","rotator"]))