name = input("What is your name?")
question = input("Hi! " + name + " , you look like you are eager to learn something CYBERSECURITY related.  Would you like an idea for what to base your learnings on today?")
answer = ""

import random

random_number = random.randint(1, 12)
if random_number == 1:
  answer = "Do some CodeAcademy!"
elif random_number == 2:
  answer = "Continue your certification training!"
elif random_number == 3:
  answer = "Hunt for a Bug Bounty!"
elif random_number == 4:
  answer = "See if there is a CTF running!"
elif random_number == 5:
  answer = "Do a HackTheBox lab!"
elif random_number == 6:
  answer = "One chapter in the web application's hacker's handbook!"
elif random_number == 7:
  answer = "Learn about a new tool!"
elif random_number == 8:
  answer = "Write a blog!"
elif random_number == 9:
  answer = "Play with an intentionally vulnerable website!"
elif random_number == 10:
  answer = "Watch a video!"
elif random_number == 11:
  answer = "Listen to a podcast!"
elif random_number == 12:
  answer = "Read an article and write a review for github blog!"
else:
  answer = "Try again!"
if name == "":
  print("Question: ", question)
else:
  print(name, "wanted to know what random learning she should do")
print("The super magic machine by Kala answered: ", answer)