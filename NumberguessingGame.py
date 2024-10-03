import random
from operator import truediv
from random import randint
i=0
n = (random.randint(0,20))
chances = 5
while chances!=0:
    num1 = int(input("What's your guess?? "))

    if num1 == n:
        print("You guessed right!\n")
        print(f"You guessed it after {i} turns ")
        break


    elif num1<n:
        print(f"No, its greater than {num1}")
        chances-=1
        i+=1
        continue
    elif num1>n:
        print(f"No, its less than {num1}")
        i+=1
        continue
    elif num1==(n-1):
        print("You're just close to it")
        chances-=1
        i+=1
        continue

if chances==0:
    print("Game Over!!")




