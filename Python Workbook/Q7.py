#define a function so when its called, the function should return a new list with all of the elements in the original list reversed

def reverse_elements(input_nums: list[int]) -> list[int]:
    return list(reversed(input_nums)) #The square brackets [] are used to create list literals directly. Thats why its list() not list[]

print(reverse_elements([1, 2, 3, 4, 5]))
