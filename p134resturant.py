a=0
b=0
c=0
d=0

while True:
    print("1)Pizza")
    print("2)Burger")
    print("3)Spaghetti")
    print("4)Lasagna")
    print("5)Done")

    op=int(input("What your order?"))

    if op==1:
        print("its $14")
        qty=int(input("how much?"))
        a=qty*14
        print(a,"$ will be your bill")

    elif op==2:
        print("its $10")
        qty=int(input("how much?"))
        b=qty*10
        print(b,"$ will be your bill")

    elif op==3:
        print("its $20")
        qty=int(input("how much?"))
        c=qty*20
        print(c,"$ will be your bill")
        
    elif op==4:
        print("its $25")
        qty=int(input("how much?"))
        d=qty*25
        print(d,"$ will be your bill")

    elif op==5:
        print("$",a+b+c+d,"WILL BE YOUR GRAND BILL.")
        break
        
    else:
        print("sorry, its not available")
