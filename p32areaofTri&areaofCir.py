print("Press 1 to find area of Triangle")
print("Press 2 to find area of Circle")
op=int(input("Press 1 or 2-->"))

if op==1:
    Height = int(input("Enter Height:"))
    Breadth = int(input("Enter Breadth:"))
    area=Height*Breadth*0.5
    print("Area of Triangle = ",area)

elif op==2:
    no = int(input("Enter the Radius:"))
    area=no*no*3.14
    print("Area of Circle = ",area)

else:
    print("Press the correct option")