class Father:
    def height(self):
        print("H")
class Mother:
    def complexionn(self):
        print("C")
class Child(Father.Mother):
    pass
c=Child()
print("Child: ")
c.height()
c.complexion()
