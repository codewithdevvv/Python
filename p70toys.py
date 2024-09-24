print("1)Battery Based Toys=440rs")
print("2)Key-based Toys=65rs")
print("3)Electrical Charging Based Toys=200rs")
product=int(input("Enter the product number:-"))
toys=int(input("How many pieces you want:-"))

if product==1:
    a=toys*440
    if a > 1000:
        print(a*10/100,"will be your total bill after 10% discount")
    else:
        print(a,"will be your total bill")
elif product==2:
    b=toys*65
    if b > 1000:
        print(b*5/100,"will be your total bill after 5% discount")
    else:
        print(b,"will be your total bill")
elif product==3:
    c=toys*200
    if c > 1000:
        print(c*10/100,"will be your total bill after 10% discount")
    else:
        print(c,"will be your total bill")
else:
    print("enter the correct product number")
    
    