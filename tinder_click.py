import os
import pyautogui
import time

#pyautogui.position(773,902)
#x=773,y=902

i=0

while i<10:
    pyautogui.click(773,902)
    time.sleep(0.2)
    i+=1


print("Happy HumpDay")
