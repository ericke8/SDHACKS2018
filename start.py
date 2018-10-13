import sys
import test
import test2
import time

print(chr(27) + "[2J")
time.sleep(0.5)
print("Welcome to ASL to Text!\n")
print("ASL to Text has two translation functions")
print("\t1). Automatic translation translates every two seconds")
print("\t2). Manual translation SPACE press for each translation")
print('\n')
print("Press the <Esc> key to terminate from translation")
print('\n')
print("Please make your selection to begin")
print('\n')
user_choice = ''
while True:
    user_choice = int(input("Select '0' for automatic and '1' for manual [0/1]: "))
    if user_choice == 0:
        break
    if user_choice == 1:
        break
    else:
        print("Your input is invalid")
        print('\n')

if user_choice == 0:
    test2.startCam()
else:
    test.startCam()
