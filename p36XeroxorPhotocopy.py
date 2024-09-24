print("Xerox")
print("Photocopy")
print("Both")
op=(input("What you wanna do?")).lower()

if op=="xerox":
    no=int(input("Enter the no. of Pages-->"))
    if no < 50:
        print(no*5,"will be your bill")
    else:
        print(no*3,"will be your bill")

elif op=="photocopy":
    no=int(input("Enter the no. of copys"))
    if no < 20:
        print(no*5,"will be your bill")
    else:
        print(no*3,"will be your bill")

elif op=="both":
   b1=b2=0
   no1=int(input("Enter the no. of Xerox"))
   no2=int(input("Enter the no. of Photocopy"))
   if no1 < 50:
       b1=no1*5
   else: 
       b1=no1*3
    
   if no2 < 20:
       b2=no2*5
   else: 
       b2=no2*3
   
   print(b1,"is your xerox bill")
   print(b2,"is your photocopy bill")
   print(b1+b2,"will per your total bill")
   
else:
    print("we cannot do that")


