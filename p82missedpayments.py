mp=int(input("Enter number of missed payments:-"))
if mp == 0:
    print("Excellent")
elif 1 <= mp <= 2:
    print("Good")
elif 3 <= mp <= 5:
    print("Fair")
else:
    print("Poor")