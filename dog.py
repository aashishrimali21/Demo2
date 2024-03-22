class Dog:
    def bark(self):
        print("Bow Bow...")
class Duck:
    def talk(self):
        print("Quack Quack...")
class Human:
    def talk(self):
        print("Hello hii...")

    def call_talk(object):
        if hasattr(object,"talk"):
            object.talk()
        elif hasattr(object,"bark"):
            object.bark()
        else:
            print("wrong object passed")

    x=Dog()
    call_talk()
    y=Duck()
    call_talk()
    z=Human()
    call_talk()

