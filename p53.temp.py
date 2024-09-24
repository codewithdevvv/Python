temp=int(input("Enter the Tempurature:-"))
if 0 >temp:
    print("freezing Atmosphere")
elif 10> temp and temp<20:
    print("very cold atmosphere")
elif temp>=20 and temp<=30:
    print("normal Atmosphere")
elif temp>=30 and temp<=40:
    print("hot atmosphere")
elif temp > 40 :
    print("very hot atmosphere ")
else:
    print("not available")