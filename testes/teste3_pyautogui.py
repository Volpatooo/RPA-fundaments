import pyautogui
import time
import os

pyautogui.press("win")
time.sleep(1)
pyautogui.write("Calculadora")
pyautogui.press("enter")
time.sleep(2)

os.makedirs('Imagens', exist_ok=True)
screenshot = pyautogui.screenshot()
screenshot.save("Imagens/screenshot_calculadora_pyautogui.png")
print("Screenshot has been Done. ")
pyautogui.hotkey("Alt","F4")