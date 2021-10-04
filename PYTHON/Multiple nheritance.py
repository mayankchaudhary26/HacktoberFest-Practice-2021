class A:
    def name(self):
        print("Hey, I am anuj")


class B:
    def edu(self):
        print(("I am studing B.E in CSE"))


class C(A, B):
    def hobbie(self):
        print("My hobies are reading manga and light novels")


obj1 = C()

obj1.name()
obj1.edu()
obj1.hobbie()
