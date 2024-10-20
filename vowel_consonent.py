#check it is a vowel or consonant
char = input("Enter a character to check Vowel or Consonant :")
vowel = ('a','e','i','o','u',)
if char in vowel:
    print(f"{char} is a Vowel ")
else :
    print(f"{char} is a Consonant")