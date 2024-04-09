#Dict.py1

def create_tuples(input_list):
    # Using list comprehension to create tuples
    output_list = [(x, x**2) for x in input_list]
    return output_list

# Example input list
input_list = [1, 2, 3]

# Calling the function and printing the output
print(create_tuples(input_list))

