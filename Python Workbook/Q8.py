#when called the function should return a new list containing only the strings from the original list
def filter_type_str(input_list: list[str | int]) -> list[str]:
    new_list = []
    for x in input_list:
        if isinstance(x, str):
            new_list.append(x)
    return new_list
        
print(filter_type_str(["hello", 1, 2,"www"]))