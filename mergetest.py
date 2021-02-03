import pyperclip
print("please enter the meeting link/personal room")
meetingId = input()
pyperclip.copy(meetingId)
text = pyperclip.paste()
print(text)
