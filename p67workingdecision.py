age=int(input("Enter your age:-"))
op=(input("Enter your gender:-")).lower()
days=input("Enter your marital status(Y/N) :-")

if op=="f":
    print("You will work only in urban areas")
    

elif op=="m":
    if 20 > age or age <30:
        print("You may work in anywhere")
    elif age > 40 or age < 60:
        print("You will work in urban areas only")
    else:
         print("Wrong age")
else:
    print("ERROR")