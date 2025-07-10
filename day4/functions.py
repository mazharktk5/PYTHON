# def avg():
#     markss1 = int(input("Enter marks of student 1: "))
#     markss2 = int(input("Enter marks of student 2: "))
#     markss3 = int(input("Enter marks of student 3: "))

#     avg = (markss1 + markss2 + markss3) / 3
#     print(f"Average marks of the students is {avg}")

# avg()


# def Greeting(name):
#     print(f"Hello {name}, welcome to the Python course!")

# Greeting("Mazhar")

# def factorial(n):
#     if(n==1 or n == 0):
#         return 1

#     return n* factorial(n-1)


# Factorial = factorial(4)
# print(Factorial)


# def greatest(a,b,c):
#     if(a>b and a>c):
#         return a
#     elif(b>a and b > c):
#         return b
#     else:
#         return c

# print(greatest(3,9,6))


# def f_to_c(f):
#     return 5 * (f-32)/9

# f = int(input("Enter temperature in F....: "))

# print(round(f_to_c(f),2))


# def sum(n):
#     if(n==1):
#         return 1
#     return sum(n-1) + n

# print(sum(3))


def pattern(n):
    if (n == 0):
        return

    print("*" * n)
    pattern(n-1)


pattern(5)
