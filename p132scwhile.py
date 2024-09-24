while True:
    print("S)Square")
    print("C)Cube")
    print("E)Exit")
    do=(input("What you wanna do:-")).lower()
    if do=="s":
        num=int(input("Square of?:-"))
        print("Square of",num,"is = ",num*num)
    elif do=="c":
        num=int(input("Cube of?:-"))
        print("Cube of",num,"is = ",num*num*num)
    elif do=="e":
        print("bye!!")
        break
    else:
        print("Choose the correct option!")