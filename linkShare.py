import pyautogui
from time import sleep
#import Pillow

#starting the skype.exe
pyautogui.press('esc', interval=0.1)
sleep(0.2)

def skypeStart():
    pyautogui.press('win', interval=0.1)
    sleep(10)
    pyautogui.write('skype')
    pyautogui.press('enter', interval=0.5)
    sleep(15)
 

def restartSkype():
    skypeStart()
    pyautogui.hotkey('ctrl', 'q')
    sleep(5)

    #restrating the skype app
    skypeStart()


    #maximize the skype window
    pyautogui.hotkey('win','up')
    sleep(5)
    

def contactSearch():
    pyautogui.hotkey('ctrl', 'shift', 's')
    sleep(3)
    pyautogui.hotkey('ctrl', 'a')
    sleep(0.5)
    pyautogui.write('Harsha Donepudi')
    sleep(5)
    pyautogui.press('enter', interval=2)
    pyautogui.press('enter', interval=2)
    sleep(10)
    pyautogui.click(794, 994)
    pyautogui.press('enter', interval=2)

#past the metting link
def shareLink():
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter', interval=1)
def main():
    print("sharing the link")
    restartSkype()
    contactSearch()
    shareLink()

if __name__ == "__main__":
    main()