import colorama
from colorama import Fore,Back

# Initialize colorama
colorama.init()

# Get user input
number = int(input("Enter the number: "))

# Check if the number is positive or negative
if number > 0:
    print(Back.GREEN , "The number is Positive")
else:
    print(Fore.RED , "The number is Negative")
