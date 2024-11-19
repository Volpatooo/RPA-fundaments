import pyautogui
import webbrowser
import time

def login_automatico(usuario, senha):
    webbrowser.open('login-html.html')
    time.sleep(3)
    campo_login = pyautogui.locateOnScreen("campo-login.png", confidence=0.8)

    if campo_login:
        pyautogui.click(campo_login) # se o campo_login for encontrado vai localizar a imagem
        pyautogui.typewrite(usuario) # depois vai escrever o usuario
    else:
        print("Campo de email não encontrado")
        return
    pyautogui.press("tab")
    pyautogui.write(senha)
    pyautogui.press("enter")
login_automatico("teteuvolpato@gmail.com", "12345")