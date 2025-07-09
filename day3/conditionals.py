# 

# p1 = "buy now"
# p2 = "click this"

# comment = input("Enter your comment: ")

# if (p1 in comment) or (p2 in comment):
#     print("You are a spammer!")
# else:
#     print("Thank you for your comment!")

# name = input("Enter your name: ")

# if(len(name) < 10):
#     print("Your name is short")
# else:
#     print("Your name is long")



# list = ["mazhar", "ali", "khan"]

# name = input("Enter your name: ")

# if(name in list):
#     print(f"{name} in the list")
# else:
#     print(f"{name} is not in the list")

marks = int(input("Enter your marks: "))

if(marks <=100 and marks >= 90):
    print("You got A+")
elif(marks < 90 and marks >= 80):
    print("You got A")
elif(marks < 80 and marks >= 70):
    print("You got B")
elif(marks < 70 and marks >= 60):
    print("You got C")
elif(marks < 60 and marks >= 50):
    print("You got D")
elif(marks<50):
    print("You are Fail")

else:
    print("Invalid marks entered")
