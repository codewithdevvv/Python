mp=int(input("Enter the Market Price:-"))

if mp > 10000:
    print(mp-20,"is the net amount")
elif mp > 70000 or mp <= 10000 :
    print(mp-15,"is the net amount")
elif mp >= 7000:
    print(mp-10,"is the net amount")
else:
    print("Enter the correct amount.")