# list =["Mazhar","Ali",2,4,5,True,False,3.14]
# print(list)
# print(list[0])
# print(list[6])

# list[3] = 10
# print(list)

# list.append("ahmad")
# print(list)
# list.insert(2, "inserted")
# print(list)
# list.remove("inserted")
# print(list)
# list.pop(4)
# print(list)
# list.sort()
# print(list)

# fruits =[]
# fruit1 = input("Enter first fruit: ")
# fruits.append(fruit1)
# fruit2 = input("Enter second fruit: ")
# fruits.append(fruit2)
# fruit3 = input("Enter third fruit: ")
# fruits.append(fruit3)
 
# fruit4 = input("Enter fourth fruit: ")
# fruits.append(fruit4)
# fruit5 = input("Enter fifth fruit: ")
# fruits.append(fruit5)
# fruit6 = input("Enter sixth fruit: ")
# fruits.append(fruit6)
# fruit7 = input("Enter seventh fruit: ")
# fruits.append(fruit7)
# print(fruits)

marks = []
for i in range(5):
    mark = int(input(f"Enter mark for student {i+1}: "))
    marks.append(mark)
    marks.sort()
print("Marks of students:", marks)

