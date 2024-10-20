character = 'QWERTYUIOPASDFGHJKLZXCVBNMmnbvcxzlkjhgfdsapoiuytrewq'
digit = '1'2','3','4','5','6','7','8','9','0'
special_character = '@','#','!','$','%','^','&','*','(',')'
char = input("Enter a character , Digit or Special Character :")
if char in character :
    print(f"{char} is a Alphabet")
elif char in digit:
    print(f"{char} is a digit")
elif char in special_character:
    print(f"{char} is a special character")
