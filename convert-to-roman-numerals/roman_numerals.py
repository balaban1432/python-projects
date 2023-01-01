# 1.
# def roman_numbers(number):

#     value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
#     symbol = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
#     roman = ""
#     i = 0
#     while number > 0:
#         div = number // value[i]
#         number = number % value[i]
#         while div:
#             roman = roman + symbol[i]
#             div = div - 1
#         i += 1
#     return roman 
    

# print("This program converts decimal numbers to Roman Numerals")
# print('To exit the program, please type "exit"')

# while True:
#     number = input("Please enter a number between 1 and 3999, inclusively :")

#     try:
#         if number.lower() == "exit":
#             print("Exiting the program... Good Bye")
#             break
#         elif int(number) > 3999 or int(number) <= 0:
#             print("Not Valid Input !!!")
#         elif 3999 > int(number) > 0: 
#             print(f"roman numerals of {int(number)} is: {roman_numbers(int(number))}")
#     except:
#         print("Not Valid Input !!!")  


# 2.
def roman_numbers(number):
    value = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    symbol = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
    roman = ""
    while number != 0:
        if value[i] <= number:
            roman += symbol[i]
            number = number - value[i]
        else:
            i -= 1
    return roman  


print("This program converts decimal numbers to Roman Numerals")
print('To exit the program, please type "exit"')

while True:
    number = input("Please enter a number between 1 and 3999, inclusively :")

    try:
        if number.lower() == "exit":
            print("Exiting the program... Good Bye")
            break
        elif int(number) > 3999 or int(number) <= 0:
            print("Not Valid Input !!!")
        elif 3999 > int(number) > 0: 
            print(f"roman numerals of {int(number)} is: {roman_numbers(int(number))}")
    except:
        print("Not Valid Input !!!")          
     