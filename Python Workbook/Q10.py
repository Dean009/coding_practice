#define a function that when called, the fuction should return the second largest number in the list. if there is no second
#largest number, the function should return None
import heapq

def get_second_largest_number(input_nums: list[int]) -> int | None:
    to_find = 2 #find the 2nd largest number
    second_largest = heapq.nlargest(to_find, input_nums)[-1] #find the largest specified numbers (2) and the -1 gets the 2nd to last one
    return second_largest
    
print(get_second_largest_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))