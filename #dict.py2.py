tuples = []

# Ask the user to input a list of integer tuples
while True:
    user_input = input("Enter a list of integer tuples (q to terminate): ")
    
    if user_input == "q":
        break
    else:
        try:
            user_tuple = tuple(map(int, user_input.split(',')))
            tuples.append(user_tuple)
        except ValueError:
            print("Invalid input. Must be integers separated by commas.")

while True:
    # Ask the user to input an integer value for k
    k = input("Enter an integer value for k: ")
    
    if k.isdigit():
        k = int(k)

        # Flatten the list of tuples
        flattened_tuples = [item for sublist in tuples for item in sublist]

        # Filter the flattened list for numbers divisible by k
        result = [num for num in flattened_tuples if num % k == 0]

        # Print the numbers that are divisible by k
        print("The numbers that are divisible by k are:", result)
        break
    else:
        print("Invalid Input!") 
