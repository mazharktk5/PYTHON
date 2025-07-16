

class Employee:
    company = "bitcoders"
    def show(self):
        print(f"Company: {self.name}")



class Student(Employee):
    company = "eb learning lab"


a = Employee()
b = Student()

print(a.company, b.company)