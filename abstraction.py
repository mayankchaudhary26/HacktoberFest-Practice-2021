from abc import ABC,abstractmethod

class A(ABC):
    def sides(self):
        pass


class B (A):
    def sides(self):
        print(("Triangle  have three sides"))


obj1 = B()
obj1.sides()