# simple lotto number selector

import random

nums = random.sample(range(1,46), 6)
nums.sort()
print(nums)

# with Num Select

import random

quan = int(input('How many Sets of Number will you get?\n>> '))
results = list()
for x in range(0, quan):
    nums = random.sample(range(1,46), 6)
    nums.sort()
    results.append(nums)

for result in results:
    print(result)

# with the winner info

import random, os

winner = random.sample(range(1, 46), 7)
winner_bonus = winner[-1]
winner = winner[:5]
winner.sort()

def printWinner():
    print(f"The Jackpot Number is {winner}\nAnd the Bonus Number is {winner_bonus}")

def fullAuto():
    trial = 0
    while True:
        cust = random.sample(range(1,46), 6)
        cust.sort()
        trial += 1
        if cust == winner:
            break
        os.system('cls')
        printWinner()
        print(f"{trial} trial. {cust} Fail")
    print(f"{trial} Trial. {cust} Jackpot!")

def semiAuto():
    pass

def Manual():
    cust = list()
    while len(cust)<6:
        cust_input = int(input("Type number in Range 1~45\n>> "))
        if not cust_input in range(1,46) or cust_input in cust:
            os.system('cls')
            print("Wrong Input, Try Again")
            os.system('cls')
            continue
        cust.append(cust_input)
    
def Rank_info(cust, winner, winner_bonus):
    if cust == winner:
        return 1
    elif 