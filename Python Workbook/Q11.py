#define a function that when called should return a string representation of the number with commas as thousand seperators
def format_number_with_commas(input_num: int) -> str:
    # Directly format the number with commas
    formatted_number = f"{input_num:,}"    #f says to format the input, : is 'how to format' and , is python built in for thousand formatting
    return formatted_number

print(format_number_with_commas(1000000000000)) 
