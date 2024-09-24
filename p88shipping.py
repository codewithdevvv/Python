km=int(input("Enter the Distence(km):-"))
kg=int(input("Enter the Weight(Kg):-"))
if kg > 5:
    print("Freight Shipping")
elif km > 100 and kg <= 5:
    print("Express Shipping")
elif km <= 100 and kg <= 5:
    print("Standard Shipping")
else:
    print("Enter the correct output")
  