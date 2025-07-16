

# class Student:
#     name = "Mazhar"
#     age = 20


# s = Student()

# s.salary = 20000

# print(s.name, s.salary)


# class Company:
#     name = "MAzhar group "
#     location = "Peshawer"
#     def getInfo(self):
#         print({self.location})


# c = Company()
# c.getInfo()  # Output: {'Peshawer'}



# class Programer:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary


# p1 = Programer("Mazhar",20,230004)
# print(p1.name,p1.age,p1.salary)
# p2 = Programer("ALi" , 23  ,23400)
# print(p2.name,p2.age,p2.salary)  



class Train:
    def __init__(self, name, speed, year):
        self.name = name
        self.speed = speed
        self.year = year
    def displayInfo(self):
            print(f"Name: {self.name}")
            print(f"Speed: {self.speed} km/h")
            print(f"Year: {self.year}")
            
            print("Train info displayed")

t = Train("mazhar" ,2000, 2005)
t.displayInfo()  # Output: Name: Mazhar Train info displayed

        
        

