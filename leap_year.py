#year is leap year or not
year = int(input("Enter a Year to check for Leap Year :"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"{year} is a leap year.")
else :
    print(f"{year} is not a leap year.")