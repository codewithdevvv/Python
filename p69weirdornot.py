def check_weird(n):
    if n % 2 != 0:  # If n is odd
        print("Weird")
    else:  # If n is even
        if 2 <= n <= 5:
            print("Not Weird")
        elif 6 <= n <= 20:
            print("Weird")
        elif n > 20:
            print("Not Weird")

# Accepting input from the user
try:
    n = int(input("Enter an integer: "))
    check_weird(n)
except ValueError:
    print("Please enter a valid integer.")

#need to understand this!!!

