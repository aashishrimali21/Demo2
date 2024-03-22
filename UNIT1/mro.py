class A(object):
    def method(self):
        print("A class method")
        super().method()

class B(object):
    def method(self):
        print("B class method")
        super().method()

class C(object):
    def method(self):
        print("C class method")

class X(A,B):
    def method(self):
        print("X class method")
        super().method()

class P(X,C):
    def method(self):
        print("P class method")
        super().method()

        newp=P()
        print=(P.mro())
        newp.method()
