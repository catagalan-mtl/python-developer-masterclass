questions = ['Who founded python?', 'What is the shortened version of "boolean" in Python?', 'what is 23+71?',
             'when was Python created?', 'To assign a variable, do we use = or ==?']

answers = ['Guido van Rossum', 'bool', '94', '1991', '=']

i = 0
score = 0
for question in questions:
    print(f"{question}")
    answer = input("> ")
    print("")
    if answer == answers[i]:
        score += 1
        print("You GOT IT!\n")
    else:
        print("OOOOOPS... wrong answer!\n")
    i += 1

if score == 5:
    print(f"AWESOME JOB, you pass with a score of {score}")
else:
    print(f"Sorry, only top score passes and you got {score}/5, try again!")
