import pyautogui
import time
import os

pyautogui.press("win")
time.sleep(2)
pyautogui.write("Bloco de Notas")
pyautogui.press("enter")
time.sleep(2)
pyautogui.write("Teste de mensagem")
time.sleep(1)

pyautogui.hotkey("ctrl", "s")
time.sleep(1)
pyautogui.press("enter")
pyautogui.hotkey("Alt", "F4")
