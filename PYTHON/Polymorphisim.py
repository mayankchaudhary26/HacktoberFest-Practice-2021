# method overloading
class multile:
    def mul(self, a = None, b = None, c = None):
        if a != None and b != None and c != None:
            print(f"sum of number is::{a+b+c}")
        elif a != None and b != None:
            print(f"sum of number is::{a+b}")


print('This is function overloading\n')
obj1 = multile()
obj1.mul(2, 3, 4)
obj1.mul(11, 4)


# Operator Overloading
class A:
    def __init__(self, num):
        self.num = num


    def __add__(self, b):
        sum1 = self.num + b.num
        print(f"\nSum of number is::{sum1}")


    def __sub__(self,b):
        sub1 = self.num - b.num
        print(f"\nSubtraction of number is::{sub1}")


print('\nThis is operator overloading ::')
obj1 = A(10)
obj2 = A(6)
a = obj1 + obj2
b = obj1 - obj2
