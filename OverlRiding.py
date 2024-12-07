class A:
    def show(Self):
        print("show from class A")
class B(A):
    def show(Self):
        super().show()
        print("show from calss B")
class C(A):
    def show(self):
        super().show()
        print("show from class C")
class D(B,C):
    def show(self):
        super().show()
        print("show from class D")
d1=D()
d1.show()