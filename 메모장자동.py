# 강제 메모장 켜서 ㅎㅎㅎ 입력력
import pyautogui
import pyperclip

print(pyautogui.position())
pyautogui.moveTo(800, 1199, 1)
pyautogui.moveTo(764, 1169, 1)
pyautogui.doubleClick()
pyperclip.copy("메모장")
pyautogui.hotkey('ctrl', 'v')
pyautogui.moveTo(753, 398, 1)
pyautogui.doubleClick()
pyperclip.copy("ㅎㅎㅎ")
pyautogui.keyDown('ctrl')
pyautogui.press('v')
pyautogui.keyUp('ctrl')
pyautogui.write("HAHAHA", interval = 0.1)