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

def factorial(n):
    if(n==1 or n == 0):
        return 1
    
    return n* factorial(n-1)

    

Factorial = factorial(4)
print(Factorial)