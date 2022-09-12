class A:
    def method(self):
        id=98888
class B:
    def method2(self):
        name="Bhargavi"
class Derived(A,B):
    def method3(self):
        college="Klu"
ob=Derived()
print(ob.method)
print(ob.method2)
print(ob.method3)
