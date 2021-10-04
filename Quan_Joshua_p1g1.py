# Quiz Creation Activity

# Quiz will have ay least 5 questions
# It will keep track or score and give a final result

import time

# Introduction
print("""Hello, Welcome to my quiz. 
I will be asking you five questions 
and we'll see what your percentage is at the end!

""")

# Set up the score counter
score = 0

# Create 6 questions and responses to user input
question = input("What is 121 + 190? \n")

if question == "311":
    print("Bingo! You nailed that question!\n")
    score += 1
else:
    print("Wrong. It is 311.\n")

time.sleep(3)

question = input("What month does Christmas fall on? \n").lower().strip("!?. ")

if question == "december":
    print("You got it right!\n")
    score += 1
else:
    print("incorrect.............\n")

time.sleep(3)

question = input("What type of cell contains no membrane bound organelles? ").lower().strip("!?. ")

if question in ("prokaryotic cell", "prokaryotes", "prokaryotic cells", "prokaryote"):
    print("You got that one correct!\n")
    score += 1
elif question in ("eukaryotic cell", "eukaryotes", "eukaryotic cells", "eukaryote"):
    print("""Close, 
    but eukaryotic cells are the type of cells that contain membrane bound organelles. 
    Wrong.
    """)
else:
    print("Wrong. The answer is prokaryotic cells.\n")

time.sleep(3)

question = input("how many net ATP does glycosis produce? ").lower().strip("!?. ")

if question == "2" or question == "two":
    print("Nice job!\n")
    score += 1
elif question == "4" or question == "four":
    print("Glycosis does produce 4 ATP but I was asking for the net amount.\nSorry, you are wrong.\n")
else:
    print("Invalid. The answer is 2 ATP\n")

time.sleep(3)

question = input("Where does the Calvin Cycle occur in the chloroplast? ").lower().strip("!?. ")

if question == "stroma":
    print("Good Job.\n")
    score += 1
elif question == "stomata":
    print("Incorrect. Stomata sounds kinda like stroma, but it is not.\n")
else:
    print("Err! The answer is stroma.\n")

time.sleep(3)

question = input("""A portion of the Earth where living things exist is called:

A) Biosphere
B) Ecosystem
C) Population

Pick one of these letters: """).lower().strip("!?. ")

if question == "a":
    print("WOOHOO!! WOW YOU GOT THAT RIGHT!!!\n")
    score += 1
elif question == "b":
    print("Yea I thought that as well, but it's wrong. ERR.\n")
elif question == "c":
    print("Im sorry, that choice is wrong.\n")
else:
    print("You did not pick one of this letters, so you got this question wrong.\n")

time.sleep(3)

# Results and farewells
percentage = (score / 6) * 100
print(f"You got {round(percentage, 2)}% right.")
print(f"{score}/6\n\n")
print("Thank you for participating in my quiz.")
print("Good Bye! :)")
