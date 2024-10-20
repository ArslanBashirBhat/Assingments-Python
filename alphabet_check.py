#char is alphabet or not
alphabets = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
char = input("Enter an alphabet :")
if char in alphabets :
    print(f"{char} is an Alphabet")
else :
    print(f"{char} is not an alphabet")