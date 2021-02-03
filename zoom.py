import pyautogui
from time import sleep
#import videoshare
#import linkShare
import os

#starting the zoom.exe
pyautogui.press('esc', interval=0.1)
sleep(0.2)

def zoomStart():
    pyautogui.press('win', interval=0.1)
    sleep(5)
    pyautogui.write('zoom')
    pyautogui.press('enter', interval=0.5)
    sleep(15)
 

zoomStart()
pyautogui.hotkey('alt', 'f4')
sleep(5)

#restrating the zoom app
zoomStart()


#maximize the zoom window
pyautogui.hotkey('win','up')
sleep(5)

#click on Home 852,44
pyautogui.click(852, 44)
sleep(2)

#start a meeting
pyautogui.click(655, 438)
sleep(5)

#share the screen
pyautogui.hotkey('alt', 's')

sleep(60)

#calling linkShare file.
sleep(5)
os.system('python linkShare.py')

#calling the video share file.
sleep(20)
os.system('python videoshare.py')

