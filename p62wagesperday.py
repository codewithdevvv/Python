age=int(input("Enter your age:-"))
op=(input("Enter your gender:-")).lower()
days=int(input("Enter your working days:-"))

if op=="m":
    if age >= 18 or age < 30:
        print(days*700,"will be your total salary credit")
    elif age >=30 or age <= 40:
        print(days*700,"will be your total salary")
    else:
        print("Wrong age")

elif op=="f":
    if age >= 18 or age < 30:
        print(days*750,"will be your total salary")
    elif age >=30 or age <= 40:
        print(days*750,"will be your total salary")
    else:
         print("Wrong age")
else:
    print("Enter the correct Gender")