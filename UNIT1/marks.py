class student:
    maarks=10
    @classmethod
    def modify(cls,name):
        print("{}scored marks".format(name,cls.marks))
        student.modify("A")
        student.modify("B")
        
