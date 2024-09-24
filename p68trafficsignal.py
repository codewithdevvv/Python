color=input("Traffic signal color:-").lower()
if color=="red":
   print("Car should STOP!")
elif color=="yellow":
   print("Car should WAIT!")
elif color=="green":
   print("Car can GO!")
else:
   print("unrecognized signal.")