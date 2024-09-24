amount=int(input("Enter purchase amount:-"))
loyal=int(input("Enter loyalty status:-"))
if loyal > 1 and amount > 2000:
    print("20% discount applied")
elif loyal <= 1 and amount> 2000:
    print("10% discount applied")
else:
    print("No discount applied")