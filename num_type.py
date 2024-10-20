#check number is POSITIVE, NEGATIVE OR ZERO
number = int(input("Enter a Number :"))
if number > 0 :
    print(f"{number} is a positive number.")
elif number < 0 :
    print(f"{number} is a negative number.")
else :
    print("number is zero")