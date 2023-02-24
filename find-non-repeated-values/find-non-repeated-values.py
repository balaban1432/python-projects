products = ["Pride and Prejudice", "To Kill a Mockingbird", "The Great Gatsby",\
"One Hundred Years of Solitude", "Pride and Prejudice", "In Cold Blood", "Wide Sargasso Sea",\
"One Hundred Years of Solitude", "Brave New World",  "The Great Gatsby", "Brave New World",\
"I Capture The Castle", "Brave New World", "The Great Gatsby", "The Great Gatsby",\
"One Hundred Years of Solitude", "Pride and Prejudice"]


print("This program finds the non-repeated (appears only once) values in a list.")

stack = []

for i in products:
    if products.count(i) > 1:
        stack.append(i)
  
set_list = set(products)
set_stack = set(stack)
result = set_list.difference(set_stack)  # result = set_list - set_stack

for i in result:
    print(i)       
