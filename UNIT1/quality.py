class Father:
    def height(self):
        print("Height is 6.00 foot")

class Mother:
    def complexion(self):
        print("Comlexion is fair")

class Child(Father.Mother):
    pass
c=child()
print("Child inherited qualities: ")
c.height()
c.complexion()
