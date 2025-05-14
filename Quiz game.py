# Quiz Game in Python

questions = ("How many elements are in the periodic table?: ",
             "which animal lays the largest egg?: ",
             "What is the most abundanr gas in earth's atomosphere?: ",
             "How many bones are in the human body?: ",
             "Which planet in the solar system is the hotest?: ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephanr", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Caebon - Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print(" Correct Answer")
    else:
        print("Incorrect answer! ")
        print(f"{answers[question_num]} is the Correct Answer")
    question_num += 1

print()
print(" ------------------ ")
print("      RESULTS ")
print(" ------------------ ")

print("Correct answers is: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Your guesses is: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your Score is:  {score}% ")
