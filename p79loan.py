num=int(input("Enter your credit score:-"))
if num > 700:
    print("Eligible for loan")
elif 699 < num and num > 600:
    print("If the score is 700 or higher,you will be eligible for loan")
elif num > 600:
    print("Not eligible for loan")
else:
    print("enter the correct creit score")
