def convert_time(time):
    value = [3600000, 60000, 1000]
    unit = [" hour/s ", " minute/s ", " second/s "]
    i = 0
    result = ""
    while time >= 1000:
        if time >= value[i]:
            result += str(time // value[i]) + unit[i]
            time = time % value[i]
        else:
            i += 1    
    return result
       

print("This program converts milliseconds into hours, minutes, and seconds")
print('To exit the program, please type "exit"')

while True:
    time = input("Please enter the milliseconds (should be greater than zero) :")

    try:
        if time.lower() == "exit":
            print("Exiting the program... Good Bye")
            break
        elif int(time) < 1:
            print("Not Valid Input !!!")
        elif int(time) < 1000 and int(time) >= 1:
            print("Just " + time + " milisecond/s")
        elif int(time) >= 1000:
            print(f"The calculated time is : {convert_time(int(time))}")         
    except:
        print("Not Valid Input !!!")       



    



