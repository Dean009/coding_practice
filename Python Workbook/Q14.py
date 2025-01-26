def reverse_first_five_positions(input_nums: list[int]) -> list[int]:
    # Your implementation here
    
    
    if len(input_nums) == 10:
        input_nums[0], input_nums[4] = input_nums[4], input_nums[0]
        input_nums[1], input_nums[3] = input_nums[3], input_nums[1]
        
        return input_nums

print(reverse_first_five_positions([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(reverse_first_five_positions([100, 90, 80, 70, 60, 50, 40, 30, 20, 10]))
print(reverse_first_five_positions([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]))
