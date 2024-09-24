money=int(input("Enter investment amount:-"))
type=input("Enter investment type:- ").lower()
if money <= 10000 and type=="savings account":
    print("Low Risk")
elif money > 10001 and 50000 > money and type=="mutual funds":
    print("Medium Risk")
elif money>50000 and type=="stocks":
    print("High Risk")
else:
    ("Enter correct amount/type")
