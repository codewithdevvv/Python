purchases=int(input("Enter total purchases:-"))
membership =int(input("Enter years of membership :-"))
if purchases>50000 and membership>2:
    print("Upgrade eligible")
else:
    print("No upgrade")