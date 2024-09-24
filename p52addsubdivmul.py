print("Press 1 for Addition")
print("Press 2 for Subtraction")
print("Press 3 for Multiplication")
print("Press 4 for Division")
op=int(input("Press the option-->"))

if op==1:
    no1=int(input("enter the number:"))
    no2=int(input("enter the number:"))
    print(" Addition = ",no1+no2)

elif op==2:
    no1=int(input("enter the number:"))
    no2=int(input("enter the number:"))
    print(" Subtraction = ",no1-no2)

elif op==3:
    no1=int(input("enter the number:"))
    no2=int(input("enter the number:"))
    print("Multiplication  = ",no1*no2)

elif op==4:
    no1=int(input("enter the number:"))
    no2=int(input("enter the number:"))
    print("Division  = ",no1/no2)

else:
    print("Wrong Option")