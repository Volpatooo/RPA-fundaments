import pyautogui
import webbrowser
import time

def login_automatico(email, senha):
    webbrowser.open('login-html.html')
    time.sleep(3)   
    x = 661 # variaveis criadas para definir aonde o mouse vai clicar
    y = 292 # variaveis criadas para definir aonde o mouse vai clicar
    pyautogui.click(x, y) # fala as coordenadas aonde o mouse vai clicar testamos isso com o arquivo monitoramneto_click_mouse.py
    pyautogui.write(email)
    pyautogui.press("tab")
    pyautogui.write(senha)
    pyautogui.press("enter")



login_automatico("teteuvolpato@gmail.com", "12345")