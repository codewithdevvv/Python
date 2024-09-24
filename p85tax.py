income=int(input("Enter your income:-"))
age=int(input("Enter your age:-"))
if income <= 30000:
    print("Low")
elif 30000 < income <= 60000:
    if 18 <= age <= 50:
        print("Medium")
    else:
        print("High")
else:
   print("High")
