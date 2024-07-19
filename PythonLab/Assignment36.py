import numpy as np

# Input list
my_list = [1, 2, 3, 4, 5]

# Convert the list to a numpy array
my_array = np.array(my_list)

# Display the numpy array
print("Numpy Array:", my_array)

# Display the first and last index
print("First element:", my_array[0])
print("Last element:", my_array[-1])

# Multiply each element by 2
multiplied_array = my_array * 2

# Display the result
print("Multiplied Array:", multiplied_array)

#Output
#Numpy Array: [1 2 3 4 5]
#First element: 1
#Last element: 5
#Multiplied Array: [ 2  4  6  8 10]
