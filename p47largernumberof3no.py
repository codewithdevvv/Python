number1=int(input("enter the first number"))
number2=int(input("enter the second number"))
number3=int(input("enter the third number"))
if number1 > number2 and number1>number3:
    print(number1,"is Greater")
elif number2 > number3 and number2>number1:
    print(number2, "is Greater")  
elif number3>number1 and number3>number2:
    print(number3,"is Greater") 
else:
    print("All are equal")