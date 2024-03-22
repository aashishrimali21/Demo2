def menu():
    print("\n")
    print("============================")
    print("============================")
    print("1=)Circle")
    print("2=)Simple Intrest")
    print("3=)Average")
    print("4=)Quit   \n")

    return int(input("Enter Choice: "))

def circle():
    r=int(input("Enter r: "))
    area=float(3.14)*r*r
    print("============================")
    print("Area of Circle : ",area)
    print("============================")

def intrest():
    amt=int(input("Enter amt: "))
    rate=int(input("Enter rate: "))
    print("============================")
    interst=float(amt*rate/100)
    print("============================")
    print("Simple Intrest : ",intrest)

def average():
    amt1=int(input("enter 1: "))
    amt2=int(input("enter 2: "))
    amt3=int(input("enter 3: "))
    sum=float(amt1+amt2+amt3)
    average=float(sum/3)
    print("Average : ",average)
    print("============================")
    print("============================")
loop=1
choice=0
while loop==1:
    choice=menu()
    if choice==1:
        circle()
    elif choice==2:
        intrest()
    elif choice==3:
        average()
    elif choice==4:
        loop=0
                

















    
