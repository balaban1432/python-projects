print("This program finds the most frequent letter in a string.")

stack = []

while True:
    word = input("Enter a string: ").lower().replace(" ", "")
    if word == "exit":
            break
    else:
        for letter in word:
            stack.append(letter)

# print(stack)
result = {}
i = 0

for k in stack:
    letter = stack[i]
    count = stack.count(stack[i])
    result.update({
        count : letter
    })
    i += 1

# print(result)
max_count = max(result.keys())  
# print(max_count)
max_letter = result[max(result.keys())]
# print(max_letter)

print(f"{max_letter} -> {max_count}")