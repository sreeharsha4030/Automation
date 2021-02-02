import pyautogui
import time

#search for video file
pyautogui.press('esc', interval=0.1)
time.sleep(0.2)

pyautogui.press('win', interval=0.1)
pyautogui.write('ks_1920')
time.sleep(5)

pyautogui.press('enter', interval=0.5)
time.sleep(5)

#select the repeat mode.
pyautogui.hotkey('ctrl', 'T')
time.sleep(2)

