temp=int(input("Enter the Tempurature:-"))
if 10>temp:
    print("Cold")
elif 10>temp or temp<25:
    print("Warm")
elif temp > 25 :
    print("hot")
else:
    print("not available")