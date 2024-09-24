print("MAX")
print("pos/neg")
op=(input("What you wanna do??")).lower()

if op=="max":
    no1=int(input("Enter the number:"))
    no2=int(input("Enter the number:"))    
    if no1 > no2:
        print(no1, "is Greater")
    else:
        print(no2, "is Greater")

elif op=="pos/neg":
    no=int(input("Enter the Number:"))

    if no > 0:
       print("The number is Positive")
    else:
       print("The number is Negative")
else:
   print("Choose the correct option")
       