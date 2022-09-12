class A:
    def method(self):
        print("this is method1")
class B(A):
    def method1(self):
        print("this is method2")
class C(B):
    def method3(self):
        print("This is Multilevel Inheritance")
ob=C()
ob.method()
ob.method1()
ob.method3()

