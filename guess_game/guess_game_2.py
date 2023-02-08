"""
1 ile 100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalışın. hak sayısı 5 olsun.
100 üzerinden puan verilsin.
"""
import random
randomnumber = random.randint(1,20)
guess_count = 0
guess_limit = 5
count = 0
score = 120

while guess_count < guess_limit:
    guess = int(input("enter your guess number: "))
    count += 1
    score -= 20
    if guess == randomnumber:
        print(f"Cangratulations!!! You won at {count}. guess.")
        print(f"Your score is {score} out of 100")
        break
    elif guess < randomnumber:
        print("up")
    elif guess > randomnumber:
        print("down")    
    guess_count += 1
else:
    print(f"Sorry, you failled! Random number is {randomnumber}")
