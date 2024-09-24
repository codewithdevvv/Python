import random
import emoji
print("Press + for Addition")
print("Press - for Subtraction")
print("Press * for Multiplication")
print("Press / for Division")
op=(input("Press the option-->"))

if op=="+":
    a=0
    b=0
    for i in range(1,6):
        x=random.randint(1,50)
        y=random.randint(1,50)
        print("No1 = ",x," No2 = ",y)
        add=x+y
        z=int(input("Enter addition:-"))
        if z==add:
            print("The entered value is correct!","\u2705")
            a=a+1
        else:
            print("The entered value is not correct","\u274C")
            b=b+1
    print("\u2705","Correct Values:-",a)
    print("\u274C","Incorrect Value:-",b)

elif op=="-":
    a=0
    b=0
    for i in range(1,6):
        x=random.randint(1,50)
        y=random.randint(1,50)
        print("No1 = ",x," No2 = ",y)
        sub=x-y
        z=int(input("Enter addition:-"))
        if z==sub:
            print("The entered value is correct!","\u2705")
            a=a+1
        else:
            print("The entered value is not correct","\u274C")
            b=b+1
    print("\u2705","Correct Values:-",a)
    print("\u274C","Incorrect Value:-",b)

elif op=="*":
    a=0
    b=0
    for i in range(1,6):
        x=random.randint(1,50)
        y=random.randint(1,50)
        print("No1 = ",x," No2 = ",y)
        mul=x*y
        z=int(input("Enter addition:-"))
        if z==mul:
            print("The entered value is correct!","\u2705")
            a=a+1
        else:
            print("The entered value is not correct","\u274C")
            b=b+1
    print("\u2705","Correct Values:-",a)
    print("\u274C","Incorrect Value:-",b)

elif op=="/":
    a=0
    b=0
    for i in range(1,6):
        x=random.randint(1,50)
        y=random.randint(1,50)
        print("No1 = ",x," No2 = ",y)
        div=x/y
        z=int(input("Enter addition:-"))
        if z==div:
            print("The entered value is correct!","\u2705")
            a=a+1
        else:
            print("The entered value is not correct","\u274C")
            b=b+1
    print("\u2705","Correct Values:-",a)
    print("\u274C","Incorrect Value:-",b)

else:
    print("Enter the correct option")

