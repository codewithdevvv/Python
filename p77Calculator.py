print("Press + for Addition")
print("Press - for Subtraction")
print("Press * for Multiplication")
print("Press / for Division")
op=(input("Press the option-->"))

if op=="+":
    no1=int(input("enter the number:"))
    no2=int(input("enter the number:"))
    print(" Addition = ",no1+no2)

elif op=="-":
    no1=int(input("enter the number:"))
    no2=int(input("enter the number:"))
    print(" Subtraction = ",no1-no2)

elif op=="*":
    no1=int(input("enter the number:"))
    no2=int(input("enter the number:"))
    print("Multiplication  = ",no1*no2)

elif op=="/":
    no1=int(input("enter the number:"))
    no2=int(input("enter the number:"))
    print("Division  = ",no1/no2)

else:
    print("Wrong Option")