import sys
import test
import test2
import time

print(chr(27) + "[2J")
time.sleep(0.5)
print("Welcome to ASL to Text!\n")
print("ASL to Text has three translation functions")
print("\t1). Automatic translation translates every two seconds")
print("\t2). Manual translation SPACE press for each translation")
print('\n')
print("Press the <Esc> key to terminate from translation")
print('\n')
print("Please make your selection to begin")
print('\n')
user_choice = ''
option3 = 2
while True:
    user_choice = input("Select your choice:\n\t [0] Manual\n\t [1] Automatic Two Sec\n\nYour Selection: ")
    try:
        user_choice = int(user_choice)
    except:
        print("Your input is invalid")
        print('\n')
        continue
    if not type(user_choice) == type(int()):
        print("Your input is invalid")
        print('\n')
        continue
    if user_choice == 0:
        break
    if user_choice == 1:
        break
    else:
        print("Your input is invalid")
        print('\n')

if user_choice == 0:
    test.startCam()
elif user_choice == 1:
    test2.startCam()
