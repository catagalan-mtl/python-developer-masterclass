# print("ready to go?")
MIN_CHARACTERS = 7
SPECIAL_CHARS = ['!', '?', '#', '@', '$', '*']
NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

PASSWORDS = ['helloWorld', 'imcisamazing69', 'ilovecookies!23', 'python1s@mazingLanguage', 'hola3#']

HAS_SPECIAL_CHAR = False
HAS_NUMBER = False
HAS_7_CHARS = False

# Write a program that checks which of the passwords inside PASSWORDS meet the 3 following criteria:
# 1. Minimum characters of 7
# 2. Must contain at least one special character (defined in SPECIAL_CHARACTERS)
# 3. Must include at least one number
# Tip: You may want to loop over PASSWORDS and use multiple if conditions

for password in PASSWORDS:
    if len(password) < 7:
        HAS_7_CHARS = False
    else:
        HAS_7_CHARS = True

    for number in NUMBERS:
        if str(number) in password:
            HAS_NUMBER = True
            break

    for special in SPECIAL_CHARS:
        if special in password:
            HAS_SPECIAL_CHAR = True
            break

    if (HAS_7_CHARS == True) and (HAS_SPECIAL_CHAR == True) and (HAS_NUMBER == True):
        print(f"{password} is a valid password")
    else:
        print(f"{password} is NOT a valid password")
