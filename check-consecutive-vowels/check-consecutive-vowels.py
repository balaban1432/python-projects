print("This program checks if a word contains consecutive vowels or not.")

word = input("Please enter a string: ").lower()

list_vowels = ["a", "e", "i", "o", "u"]

stack = []

for k in word:
    if k in list_vowels:
        stack.append(k)
        if len(stack) == 2:
           break    
    elif k not in list_vowels:
        if len(stack) != 0:
            stack.pop()


if stack == []:
    print("negative")
elif len(stack) == 1:
    print("negative")   
else:
    print("positive")           
 