# tuple = ('apple', 'banana', 'cherry')
# print("Tuple:", tuple)
# print("Type:", type(tuple))

# # Accessing elements in a tuple
# print("First element:", tuple[0])
# print("Last element:", tuple[-1])
# print("Slicing tuple:", tuple[1:3])  # Slicing the tuple

# changing a tuple

# Tuples are immutable, so we cannot change elements directly.
# However, we can convert it to a list, change it, and convert it back to
# a tuple.
# tuple = ('apple', 'banana', 'cherry')
# tuple_list = list(tuple)  # Convert tuple to list
# tuple_list[1] = 'blackcurrant'  # Change the second element

# tuple = tuple(tuple_list)  # Convert list back to tuple
# print("Tuple after changing second element:", tuple_list)


# fruits = ("apple", "banana", "cherry")

# # (green, yellow, red) = fruits

# # print(green)
# # print(yellow)
# # print(red)

# fruits.count("apple")  # Count occurrences of "apple"