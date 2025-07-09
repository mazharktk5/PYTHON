# 

p1 = "buy now"
p2 = "click this"

comment = input("Enter your comment: ")

if (p1 in comment) or (p2 in comment):
    print("You are a spammer!")
else:
    print("Thank you for your comment!")