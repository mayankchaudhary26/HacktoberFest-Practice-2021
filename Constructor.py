class Employee:
    def __init__(self, name, age, salary, gender):
        
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender
    
    def employee_details(self):
        print("Name of Employee",self.name)
        print("age of Employee", self.age)
        print("salary of Employee", self.salary)
        print("gender of Employee", self.gender)

e1 = Employee('Yuvraj',27,85000,'male')
e1.employee_details()