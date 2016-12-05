# Create a function that takes a list as a parameter,
# and returns a new list with every second element from the original list.
# It should raise an error if the parameter is not a list.
# Example: with the input [1, 2, 3, 4, 5] it should return [2, 4].

def pick_every_second_elements(input_list):

    if type(input_list) is not list:
        raise TypeError('The parameter is not a list!')

    result_list = []

    for item in range(len(input_list)):
        if (item + 1)  % 2 == 0:
            result_list.append(input_list[item])

    return result_list

print(pick_every_second_elements([1, 2, 3, 4, 5]))
