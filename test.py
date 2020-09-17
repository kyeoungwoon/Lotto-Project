import random

START = 1
END = 10

print("Welcome to the Number Game")
ans = random.randint(START, END)
cust = int(input("Guess the Number >> "))
if ans == cust:
    print("Correct")
else:
    print("Wrong")

    