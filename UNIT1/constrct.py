class student:
    def __init_(self,nm='.',ag=15,m=0):
        self.name=nm
        self.age=ag
        self.mmarks=m

    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Marks: ",self.marks)

        s=student("A",18,49)
        s.display()
        s1=student("B",19,39)
        s1.display()
