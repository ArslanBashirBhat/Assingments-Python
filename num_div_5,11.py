#check number is divisible by 5 and 11
number = int(input("Enter a Number :"))
if number % 5 == 0 :
    print(f"{number} is divisible by 5")
elif  number % 5 != 0:
    print(f"{number} is not divisible by 5")
if number % 11 ==0:
    print(f"{number} is divisible by 11")
elif number % 11 != 0:
    print(f"{number} is not divisible 11")
