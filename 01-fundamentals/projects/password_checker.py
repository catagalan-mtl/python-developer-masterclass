# print("ready to go?")
MIN_CHARACTERS = 7
SPECIAL_CHARS = ['!', '?', '#', '@', '$', '*']
NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

PASSWORDS = ['helloWorld', 'imcisamazing69', 'ilovecookies!23', 'python1s@mazingLanguage']

HAS_SPECIAL_CHAR = False
HAS_NUMBER = False
HAS_7_CHARS = False

# Write a program that checks which of the passwords inside PASSWORDS meet the 3 following criteria:
# 1. Minimum characters of 7
# 2. Must contain at least one special character (defined in SPECIAL_CHARACTERS)
# 3. Must include at least one number
# Tip: You may want to loop over PASSWORDS and use multiple if conditions

def check_length(password):
    if len(password) < 7:
        print(f"{password} is not a valid password")
    elif len(password) >= 7:
        return 1

def check_special(password):


for password in PASSWORDS:
    if check_length(password):
        print(f"{password} is a valid password")
