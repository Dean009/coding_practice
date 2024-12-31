def get_longest_string(input_strs: list[str]) -> str:
    size = -1
    for x in input_strs:
        if len(x) > size:
            size = len(x)
            res = x #assign res to the value of x (the current word) due to the others being an int
    return (res)

print(get_longest_string(["cat", "dog", "bird", "crocodile"]))
