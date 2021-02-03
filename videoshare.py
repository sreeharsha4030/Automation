import pyautogui
from time import sleep

def videoShare():
#search for video file
    pyautogui.press('esc', interval=0.1)
    sleep(0.2)

    pyautogui.press('win', interval=0.1)
    sleep(5)
    pyautogui.write('ks_1920')
    sleep(5)

    pyautogui.press('enter', interval=0.5)
    sleep(5)
    
    pyautogui.hotkey('win', 'up')

    #select the repeat mode.
    pyautogui.hotkey('ctrl', 'T')
    sleep(2)
    
    #making it full screen
    #pyautogui.moveTo(1058, 467)
    pyautogui.doubleClick(1058, 467)
    sleep(2)
    pyautogui.doubleClick(1058, 467)

def main():
    print("Starting the video share")
    playingVideo = videoShare()
    

if __name__ == "__main__":
    main()