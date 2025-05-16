print("Let's start a quiz!")
score = 0

print("First Question, who is the President of the USA? ")
answer = input()
if answer.lower() == "donald trump":
    print("Correct you earn 1 Point!   ")
    score += 1
else:
    print("Incorrect you earn 0 Points!  ")

print("Second Question, who built the Statue of Liberty?   ")
answer = input()
if answer.lower() == "france":
    print("Correct you earn 1 Point!   ")
    score += 1
else:
    print("Incorrect you earn 0 Points!  ")

print("Third Question, who plays Captain America in the Marvel Movies?    ")
answer = input()
if answer.lower() == "chris evans":
    print("Correct you earn 1 Point!   ")
    score += 1
else:
    print("Incorrect you earn 0 Points!  ")

print("Fourth Question, what is the Capital of Japan? ")
answer = input()
if answer.lower() == "tokyo":
    print("Correct you earn 1 Point!   ")
    score += 1
else:
    print("Incorrect you earn 0 Points!  ")

print("Final Question! Don't get it wrong, who is the CEO of OpenAI?   ")
answer = input()
if answer.lower() == "sam altman":
    print("Correct you earn 1 Point!   ")
    score += 1
else:
    print("Incorrect you earn 0 Points!  ")

print("You have completed the quiz! ")
print(" Your final score is: " + str(score) + "/5")
print("Come back for more quizess!")