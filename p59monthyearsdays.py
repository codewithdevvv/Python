def is_leap_year(year):
    """Check if a year is a leap year."""
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def days_in_month(month, year):
    """Return the number of days in a given month of a year."""
    # Days in each month, index 0 is January, index 11 is December
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Adjust for leap year if the month is February
    if month == 2 and is_leap_year(year):
        return 29
    return month_days[month - 1]

# Input month and year
month = int(input("Enter the month (1-12): "))
year = int(input("Enter the year: "))

# Output the number of days in the month
days = days_in_month(month, year)
print(f"The number of days in month {month}, year {year} is: {days}")
