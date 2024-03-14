import pyautogui
import threading
import datetime
import time

screenSize = pyautogui.size()
hour = datetime.datetime.now().hour

def moveMouse():
    pyautogui.moveTo(5, screenSize[1], duration = 1)

def moveMouse2():
    pyautogui.moveTo(800, 5, 2)

def clickMouse():
    pyautogui.click(button='right')

def main():    
    if hour == 17 or hour == 12:
        print("end of day reached")
        quit()
    else:
        threading.Timer(5.0, moveMouse).start()
        time.sleep(30)
        clickMouse()
        threading.Timer(5.0, moveMouse2).start()
        time.sleep(30)
        clickMouse()

while (hour != 17 or hour != 12):
    main()
