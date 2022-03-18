import pyautogui 
import time

word = input("what word would you like to see:\n")
times = int(input("How many times would you like to see it:\n"))

for i in range(0,times):
    time.sleep(5)
    pyautogui.typewrite(word)
    pyautogui.typewrite("\n")
    i = i + 1
    times = (str(i))
    print (word, "#", times, "printed\n")