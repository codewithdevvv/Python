def add():
    num1=int(input("Enter first number:-"))
    num2=int(input("Enter second number:-"))
    print(num1+num2,"Will be th adition")

def areaoftri():
    Height = int(input("Enter Heigth:-"))
    Breadth = int(input("Enter Breadth:-"))
    area=Height*Breadth*0.5
    print("Area of Triangle = ",area)

print("Press 1 for area of add")
print("Press 2 for area of tri")
op=int(input("Enter opt =>"))
if op==1:
    add()
elif op==2:
    areaoftri()