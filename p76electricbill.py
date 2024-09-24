units=int(input("enter the electric units:-"))
if units < 100:
    print("FREE")
elif units < 200:
    print(units*2,"rs will be your bill")
elif units < 300:
    print(units*5,"rs will be your bill")
else:
    print("enter ur correct units")