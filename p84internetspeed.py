speed=int(input("Enter Internet Speed:-"))
if speed <= 5:
    print("Slow")
elif 6 <= speed <= 20:
    print("Average")
elif 21 <= speed <= 50:
    print("Fast")
else:
    print("very fast")
    