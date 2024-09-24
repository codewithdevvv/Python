print("Pizza")
print("Burger")
print("Spaghetti")
print("Lasagna")
op=int(input("What your order?"))

if op==1:
    print("its $14")
    qty=int(input("how much?"))
    print(qty*14,"$ will be your total bill")
elif op==2:
    print("its $10")
    qty=int(input("how much?"))
    print(qty*10,"$ will be your total bill")
elif op==1:
    print("its $20")
    qty=int(input("how much?"))
    print(qty*20,"$ will be your total bill")
elif op==4:
    print("its $25")
    qty=int(input("how much?"))
    print(qty*25,"$ will be your total bill")
      
else:
    print("sorry, its not available")
