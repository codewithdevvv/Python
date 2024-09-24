def sumofdigit():
    num=int(input("Enter the Number:-"))
    sum = 0
    while num > 0:
        sum += num % 10  
        num //= 10  
    print("The sum of digits is:", sum)

def add():
    num1=int(input("Enter the Number1:-"))
    num2=int(input("Enter the Number2:-"))
    print("Add = ",num1+num2)

def areaoftriangle():
    Height = 10
    Breadth = 8
    area=Height*Breadth*0.5
    print("Area of Triangle = ",area)

def areaofcircle():
    radius=int(input("enter radius:-"))
    print("Area of circle=",radius*radius*3.14)

def max2():
    number1=int(input("enter the first number"))
    number2=int(input("enter the second number"))

    if number1 > number2:
        print(number1,"is greater")
    else:
        print(number2,"is greater")

def max3():
    num1=int(input("Enter the first number:-"))
    num2=int(input("Enter the second number:-"))
    num3=int(input("Enter the third number:-"))
    if num1>num2 and num1>num3:
        print(num1,"Is Greater")
    elif num2>num3 and num2>num1:
        print(num2,"Is Greater")
    elif num3>num1 and num3>num2:
        print(num3,"Is Greater")
    else:
        print("Enter correct Number")

def table():
    num=int(input("Table of which Number:-"))
    for i in range(1,11):
        print(num," x ",i," = ",num*i)

def evenodd():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(num,"is even")
    else:
       print(num,"is odd")

def posneg():
    no=int(input("Enter the number"))
    if no > 0:
      print("number is positive")
    else:
      print("number is negative")

def leapyear():
    year=int(input("Enter the year:-"))
    if (year % 400 == 0) and (year % 100 == 0):
       print(year,"is a leap year".format(year))
    elif (year % 4 ==0) and (year % 100 != 0):
         print(year,"is a leap year")
    else:
         print(year,"is not a leap year")

def square():
    num=int(input("Enter a number:-"))
    print(num*num,"is square of",num)


sumofdigit()
add()
sumofdigit()
areaoftriangle()
areaofcircle()
max2()
max3()
table()
evenodd()
posneg()
leapyear()
square()
"""
areaoftri
areaofcircle
max2
max3
table
oddeven
posneg
leapyear
square


=================

add
sub
mul
div

"""