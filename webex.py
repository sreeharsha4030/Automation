import pyautogui
from time import sleep
import pyperclip
#import videoshare
#import linkShare
import os

#starting the webex.exe
pyautogui.press('esc', interval=0.1)
sleep(0.2)

def webexStart():
    pyautogui.press('win', interval=0.1)
    sleep(5)
    pyautogui.write('webex')
    pyautogui.press('enter', interval=0.5)
    sleep(15)
 

webexStart()
pyautogui.hotkey('alt', 'f4')
sleep(5)

#restrating the webex app
webexStart()

#get the meeting info
print("please enter the meeting link/personal room")
meetingId = input()
pyperclip.copy(meetingId)
sleep(10)

#searching for box to enter the meeting number.
pyautogui.click('joinmeeting.png')
pyautogui.press('enter', interval = 0.5)
sleep(10)

#enter the meeting id
copiedLink = pyperclip.paste()
pyautogui.write(copiedLink)
sleep(5)
pyautogui.press('enter', interval = 0.5)


#maximize the window.
pyautogui.hotkey('win', 'up')
sleep(10)

pyautogui.hotkey('ctrl', 'shift', 'd')
sleep(20)

#calling videoshare file
os.system('python videoshare.py')