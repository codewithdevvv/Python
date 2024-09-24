print("Press 1 for square")
print("PRess 2 for cube")
op=int(input("Enter option =>"))

if op==1:
    no=int(input("Enter the Digit-->"))
    print("Square = ",no*no)
elif op==2:
    no=int(input("Enter the Digit-->"))
    print("Cube = ",no*no*no)
else:
    print("Wrong option")
