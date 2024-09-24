import random
a=0
b=0
for i in range(1,6):
    x=random.randint(1,50)
    y=random.randint(1,50)
    print("No1 = ",x," No2 = ",y)
    op=random.randint(1,4)
    add=x+y
    sub=x-y
    mul=x*y
    div=x*y
    
    if op==1:
        
        z=int(input("Enter Addition:-"))
        if z==add:
            print("The entered value is correct!")
            a=a+1
        else:
            print("The entered value is not correct")
            b=b+1

        
    elif op==2:
        
        z=int(input("Enter Subtraction:-"))
        if z==sub:
            print("The entered value is correct!")
            a=a+1
        else:
            print("The entered value is not correct")
            b=b+1

    elif op==3:
        
        z=int(input("Enter the Multiplaction:-"))
        if z==mul:
            print("The entered value is correct!")
            a=a+1
        else:
            print("The entered value is not correct")
            b=b+1
    
    elif op==4:
        
        z=int(input("Enter the Division:-"))
        if z==div:
            print("The entered value is correct!")
            a=a+1
        else:
            print("The entered value is not correct")
            b=b+1

print("Correct Values:-",a)
print("Incorrect Value:-",b)



    