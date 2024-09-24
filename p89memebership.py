print("Gold")
print("Silver")
print("Bronze")
mem=input("Enter your Membership:-").lower()
if mem=="gold":
    print("Full Access")
elif mem=="silver":
    print("Limited Access")
elif mem=="bronze":
    print("Minimal Access")
else:
    print("Enter the correct option")