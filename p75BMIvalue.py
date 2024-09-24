weight=int(input("Enter your Weight:-"))
height=int(input("Enter your Height:-"))
if 18.5 > weight:
    print("underweight")
elif weight > 18.5 and weight < 25:
    print("normal weight")
elif weight > 25 and weight < 30:
    print("slightly overweight")
elif weight > 30 and weight < 35:
    print("you are obese")
elif weight > 35:
    print("you have clinically obese")
else:
    print("YOU ARE F**KING FAT.")