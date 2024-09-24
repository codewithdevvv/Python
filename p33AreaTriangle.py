print("Press t to find area of Triangle")
print("Press circle to find area of Circle")
op=input("Press -->").lower()

if op=="t":
    Height = int(input("Enter Height:"))
    Breadth = int(input("Enter Breadth:"))
    area=Height*Breadth*0.5
    print("Area of Triangle = ",area)

elif op=="circle":
    no = int(input("Enter the Radius:"))
    area=no*no*3.14
    print("Area of Circle = ",area)

else:
    print("Press the correct option")