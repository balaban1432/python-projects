# bilgisayar 1 den 5 e kadar bir sayı seçip tahmin isteyecek(tahmin sayısı 3 olacak):


import random
randomnumber = random.randint(1, 5) 
guesscount = 0
guesslimit = 3
while guesscount < guesslimit:
    guess = int(input("Enter your guess: "))   
    if guess == randomnumber:
        print("You won!")
        break
    guesscount += 1
else:
     print("Sorry, you failled!")    