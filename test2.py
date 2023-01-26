class A:
    name=""
    def _init_(self):
        print("I am from class A")
    def m(self):
        print("I am method from class A")

class B(A):
    def _init_(self):
        super()._init_()
        print("I am from class B")
    def m(self):
        super().m()
        print("I am method from class B")

class C(B):
    def _init_(self):
        super()._init_()
        print("I am from class C")
    def m(self):
        super().m()
        print("I am method from class C")

#obj = A()
obj = C()
o=B()
ob = A()

print(type(obj)==type(ob))
print(type(obj)==type(o))
print(type(obj)==type(ob))