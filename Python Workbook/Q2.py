#define a function sum_if_less_than_fifty that thakes two parameteres
def sum_if_less_than_fifty (num_one: int, num_two: int) -> int | None: #this return value is only for python 3.10 and above
    if num_one + num_two < 50:
        return num_one + num_two
    else:
        return None

print (sum_if_less_than_fifty(20, 30))