# i = 0

# while i < 5:
#     print(f"Hello{i}")
#     i += 1

# list = ["mazhar", "ali", "khan",3 ,4, 5, 6, 7, 8, 9, 10]


# i = 0
# while i < len(list):
#     print(f"Hello {list[i]}")
#     i += 1

# for i in range(5):
#     print(i)

# for i in range(5, 10):
#     print(i)

# for i in range(0,100,5):
#     print(i)


# name = "mazhar"

# for i in name:
#     print(i)

# else:
#     print("Loop completed successfully")

# for i in range(20):
#     if i == 10:
#         print("Loop is breaking")
#         break
#     print(i)


# for i in range(20):
#     if i == 10:

#         print("Loop is breaking")
#         continue
#     print(i)

# num = int(input("Enter a number: "))
# for i in range(1,11):
#     table = f"{num} x {i} = {num * i}"
#     print(table)

# num = int(input("Enter a number: "))
# i = 1
# while i <= 10:
#     table = f"{num} x {i} = {num * i}"
#     print(table)
#     i += 1


# num = int(input("Enter a number: "))

# for i in range(2,num):
#     if(num % i ==0):
#         print(f"{num} is not a prime number")
#         break
# else:
#     print(f"{num} is a prime number")

# num = int(input("Enter a number: "))
# i = 1
# sum = 0
# while i <= num:
#     if num % i == 0:
#         sum += i
#     i += 1
# print(f"Sum of divisors of {num} is {sum}")

# num = int(input("Enter a number: "))
# product = 1

# for i in range(1,num + 1):
#      product *= i
#      print(product)
# print(f"Factorial of {num} is {product}")

# num = int(input("Enter a number: "))
# for i in range(1, num + 1):
#     print(" " * (num - i) + "*" * (2 * i - 1))

# num = int(input("Enter a number: "))
# for i in range(1,num + 1):
#     print("*" * i)


num = int(input("Enter a number: "))


for i in range(1, 11):
    table = f"{num} x {11-i} = {num * (11-i)}"
    print(table)
   

