# Given a list of integers, return the highest and lowest numbers in the array
# without using max() or min()

# Define the funtion
def return_max_min(num_array):
    # Sort the array from smallest to largest
    num_array.sort()
    # Return only the first(min) and last(max) number
    return [num_array[0], num_array[-1]]

# Test
# my_list = [3, 50, 20, 100, -10, 100]
# print(return_max_min(my_list))