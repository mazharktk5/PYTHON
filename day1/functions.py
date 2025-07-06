
def my_func():
    """"
    This function does nothing but serves as a placeholder.
    """
    pass


my_func()

# def another_func():

#     print("This is another function.")

# another_func()


# def name(name):
#     name = input("Enter your name: ")
#     print(f"Hello, {name}!")


# name(name)

# def name(*kids):
#     """
#     This function takes first and last name as input and prints a greeting.
#     """
#     print(f"Hello, {kids[4]}!")

# name("Mazhar", "saad", "Khan", "Ahmed", "Ali")


# def country(default_country="Pakistan"):
#     """
#     This function takes a country name as input and prints a greeting.
#     """
#     print(f"Hello, {default_country}!")


# country("India")
# country("Bangladesh")
# country("Sri Lanka")
# country()

# def food(food):
#     for item in food:
#         print(f"I love {item}!")

    
    
# fruits = ["apple", "banana", "orange", "grape"]

# food(fruits)

# def add_numbers(a, b):
#     """
#     This function takes two numbers as input and returns their sum.
#     """
#     return a + b
# def multiply_numbers(a, b):
#     """ This function takes two numbers as input and returns their product."""
#     return a * b
# def divide_numbers(a, b):
#     """

#     This function takes two numbers as input and returns their quotient.
#     """
#     if b == 0:
#         return "Cannot divide by zero"
#     return a / b

# print(add_numbers(5, 3))  # Output: 8
# print(multiply_numbers(5, 3))  # Output: 15
# print(divide_numbers(5, 3))  # Output: 1.6666666666666667
# print(divide_numbers(5, 0))  # Output: Cannot divide by zero

# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("Recursion Example Results:")
# tri_recursion(6)

# tri_recursion(6) ⏳ (waits for tri_recursion(5))
#  └── tri_recursion(5) ⏳ (waits for tri_recursion(4))
#       └── tri_recursion(4) ⏳
#            └── tri_recursion(3) ⏳
#                 └── tri_recursion(2) ⏳
#                      └── tri_recursion(1) ⏳
#                           └── tri_recursion(0) ✅

