print("This program finds the largest number among the 5 numbers given by the user")
print("please enter the five numbers you want consecutively")

count = 0
user_limit = 5
my_list = []

while count < user_limit:
    try:
        number = input("enter your numbers: ")
        my_list.append(int(number))
        count += 1
    except:
        print("Not Valid Input !!!")   


# print(my_list)
my_list.sort()
# print(my_list)

print(f"The largest number is {my_list[4]}")