def add():
    num1=int(input("Enter first number:-"))
    num2=int(input("Enter second number:-"))
    print(num1+num2,"will be the addition")

def sub():
    num1=int(input("Enter first number:-"))
    num2=int(input("Enter second number:-"))
    print(num1-num2,"will be the subtraction")

def mul():
    num1=int(input("Enter first number:-"))
    num2=int(input("Enter second number:-"))
    print(num1*num2,"will be the multiplaction")

def div():
    num1=int(input("Enter first number:-"))
    num2=int(input("Enter second number:-"))
    print(num1/num2,"will be the division")

print("Press 1 for addition")
print("Press 2 for Subtraction")
print("Press 3 for Multiplaction")
print("Press 4 for Division")
op=int(input("Press the option:"))

if op==1:
    add()
elif op==2:
    sub()
elif op==3:
    mul()
elif op==4:
    div()
else:
    print("Enter the correct option")