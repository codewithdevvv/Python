num=int(input("Enter the Number:-"))
if 10 > num:
    print("Low")
elif 10 > num or num < 20:
    print("Medium")
elif 20 > num or num < 30:
    print("High")
else:
    print("Out of range")