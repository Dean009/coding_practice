def sum_even(input_name : list[int]) -> int:
    sum_of = 0
    for select in input_name:
        if select % 2 == 0:
            sum_of = sum_of + select
    return sum_of
            
print(sum_even([1,2,3,4,5,6,7,8,9,10]))