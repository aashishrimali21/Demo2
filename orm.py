class a(object):
    def method(self):
        print("A class")
        super().meathod()
class b(object):
    def method(self):
        print("B class")
        super().method()
class c(object):
    def method(self):
        print("C class")
class x(a,b):
    def method(self):
        print("X class")
        super().method()
class P(x,c):
    def method(self):
        print("P class")
        super().method()
    newp=P()
    print=(P.mro())
    newp.method()
