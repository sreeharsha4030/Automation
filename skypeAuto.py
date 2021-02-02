import pyautogui
import time
#import Pillow

#starting the skype.exe
pyautogui.press('esc', interval=0.1)
time.sleep(0.2)

def skypeStart():
    pyautogui.press('win', interval=0.1)
    pyautogui.write('skype')
    pyautogui.press('enter', interval=0.5)
    time.sleep(15)
 

skypeStart()
pyautogui.hotkey('ctrl', 'q')
time.sleep(5)

#restrating the skype app
skypeStart()


#maximize the skype window
pyautogui.hotkey('win','up')


#to find the position of the cursor
pyautogui.position()
#Point(x=157, y=258)

#clicking on Meetnow
pyautogui.click(120, 206)
time.sleep(1)


#click on host meeting
pyautogui.click(145, 220)
time.sleep(10)

#click on copying the meeting link
pyautogui.click(769, 571)
time.sleep(1)
#Point(x=714, y=783)

#click on start metting
pyautogui.click(694, 739)
time.sleep(5)

#search for contact to share the meeting link
pyautogui.hotkey('ctrl', 'shift', 's')
time.sleep(3)
pyautogui.hotkey('ctrl', 'a')
time.sleep(0.5)
pyautogui.write('Harsha Donepudi')
time.sleep(5)
pyautogui.press('enter', interval=2)
pyautogui.press('enter', interval=2)
time.sleep(10)
pyautogui.click(794, 994)
pyautogui.press('enter', interval=2)

#past the metting link
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter', interval=1)

#start the screen share
pyautogui.click(1766, 293)
time.sleep(2)
pyautogui.click(1044, 818)
