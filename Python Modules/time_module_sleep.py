import time

#Create a program that prints out Hello  every two seconds.
# while True:
#     print("Hello")
#     time.sleep(2)


"""Create a program that once executed the programs prints Hello  instantly first, then it prints it after 1 second, then after 2, 3, and then the program prints out the message "End of the Loop" and stops.

Expected output: 

Hello
Hello
Hello
Hello
End of Loop

Hint: Include an if  statement inside the loop and a break  statement inside the conditional.

"""
i = 0
while True:
    if i <= 3 :
        print("Hello")
        i += 1
        time.sleep(i)

    else:
        print("End of loop")
        break

#more efficient sol
i = 0
while True:
    print("Hello")
    i += 1
    time.sleep(i)
    if i>3 :
        print("End of loop")
        break
