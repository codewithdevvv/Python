def add(num1,num2):
    print(num1+num2,"will be the addition")

def max2(num1,num2):
    if num1>num2:
        print("num1 is greater")
    else:
        print("num2 is greater")

num1=int(input("Enter first number:-"))
num2=int(input("Enter second number:-"))

add(num1,num2)
max2(num1,num2)