import sys
import test
import test2

print("Welcome to ASL to Text")
print("ASL to Text can translate automatically or manaully")
print("Automatic translation translates every two seconds")
print("Manual translation requires the SPACE bar to be pressed for each translation")
user_choice = ''
while True:
    print('\n')
    user_choice = int(input("Select '0' for automatic and '1' for manual [0/1]: "))
    if user_choice == 0:
        break
    if user_choice == 1:
        break

if user_choice == 0:
    test2.startCam()
else:
    test.startCam()
