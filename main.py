import pyautogui
import webbrowser
import time

message = input("Type what to spam: ")
repeats = int(input("Type the no. of times of the message:"))
delay = int(input("Delay between every msg(In Miliseconds): "))

isLoaded = input("Press enter if ready:")



print("Spam will begin after 5 seconds.")

time.sleep(5)

for i in range (0,repeats):
    if message != "":
        pyautogui.typewrite(message)
        pyautogui.press("enter")
    else:
        pyautogui.hotkey('ctrl','v')
        pyautogui.press("enter")

    time.sleep(delay/1000)

print("Done")
