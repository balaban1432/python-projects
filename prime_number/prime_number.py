"""
girilen bir sayının asal sayı olup ulmadığını kontrol edin.
"""

number = int(input("enter a number: "))
isprime = True

if number == 1:
    isprime = False

for i in range(2,number):
        if number % i == 0:
            isprime = False
            break

if isprime:
    print("The number is prime.")
else:
    print("The number is not prime.")