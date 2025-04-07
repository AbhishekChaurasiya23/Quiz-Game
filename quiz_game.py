print("Welcome, Computer Quiz Game.")

playing = input("Do you want to play? (yes/no) ").lower()
score =0

if playing != "yes":
    quit()

print("Okay, Let's play!")

quesion_1 = input("What is CPU? ").lower()
if quesion_1 == "central processing unit":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

quesion_2 = input("What is GPU ").lower()
if quesion_2 == "graphical processing unit":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

quesion_3 = input("What is PSU ").lower()
if quesion_3 == "power supply":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

quesion_4 = input("What is RAM ").lower()
if quesion_4 == "random acessed memory":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")


print("you got " + str(score) + " answer correct!")