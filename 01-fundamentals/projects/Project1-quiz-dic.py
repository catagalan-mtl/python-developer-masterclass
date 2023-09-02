quiz = {
    'Who founded python?': 'Guido van Rossum',
    'What is the shortened version of "boolean" in Python?': 'bool',
    'what is 23+71?': '94',
    'when was Python created?': '1991',
    'To assign a variable, do we use = or ==?': '='
}

i = 0
score = 0
for question, answer in quiz.items():
    print(f"{question}")
    your_answer = input("> ")
    print("")
    if your_answer == answer:
        score += 1
        print("You GOT IT!\n")
    else:
        print("OOOOOPS... wrong answer!\n")
    i += 1

if score == 5:
    print(f"AWESOME JOB, you pass with a score of {score}/5!!!\n")
else:
    print(f"Sorry, only top score passes and you got {score}/5, try again!\n")
