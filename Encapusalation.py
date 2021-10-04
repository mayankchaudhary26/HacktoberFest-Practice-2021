# Encapusalation 
class A:
    def __init__(self):
        self.__age = 10

    
    def changeAge(self,a):
        self.__age = a


    def showAge(self):
        print((f"Age is --> {self.__age}"))


obj1 = A()
obj1.showAge()
obj1.__age = 12   # private does not change

obj1.showAge()
obj1.changeAge(18)   # pprivate change by calling function
obj1.showAge()
