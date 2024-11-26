import pyautogui
import webbrowser
import time

def login_automatico(first_name, role_company, email, address, phone_number, company_name, last_name):
    webbrowser.open('https://rpachallenge.com/')
    time.sleep(1.5)   
    campo_login = pyautogui.locateOnScreen("first-name.png", confidence=0.8)
    if campo_login:
        time.sleep(1.5)
        pyautogui.click(campo_login) # se o campo_login for encontrado vai localizar a imagem
        pyautogui.typewrite(first_name) # depois vai escrever o usuario
    else:
        print("Campo de nome não encontrado")
        return
    
    campo_login = pyautogui.locateOnScreen("funcao-empresa.png", confidence=0.8)
    if campo_login:
        time.sleep(1.5)
        pyautogui.click(campo_login) # se o campo_login for encontrado vai localizar a imagem
        pyautogui.typewrite(role_company) # depois vai escrever o usuario
    else:
        print("Campo de função não encontrado")
        return
    
    campo_login = pyautogui.locateOnScreen("email.png", confidence=0.8)
    if campo_login:
        time.sleep(1.5)
        pyautogui.click(campo_login) # se o campo_login for encontrado vai localizar a imagem
        pyautogui.typewrite(email) # depois vai escrever o usuario
    else:
        print("Campo de email não encontrado")
        return
    
    campo_login = pyautogui.locateOnScreen("endereço.png", confidence=0.8)
    if campo_login:
        time.sleep(1.5)
        pyautogui.click(campo_login) # se o campo_login for encontrado vai localizar a imagem
        pyautogui.typewrite(address) # depois vai escrever o usuario
    else:
        print("Campo de endereço não encontrado")
        return
    
    campo_login = pyautogui.locateOnScreen("phone-number.png", confidence=0.8)
    if campo_login:
        time.sleep(1.5)
        pyautogui.click(campo_login) # se o campo_login for encontrado vai localizar a imagem
        pyautogui.typewrite(phone_number) # depois vai escrever o usuario
    else:
        print("Campo de telefone não encontrado")
        return
    
    campo_login = pyautogui.locateOnScreen("company-name.png", confidence=0.8)
    if campo_login:
        time.sleep(1.5)
        pyautogui.click(campo_login) # se o campo_login for encontrado vai localizar a imagem
        pyautogui.typewrite(company_name) # depois vai escrever o usuario
    else:
        print("Campo de nome da empresa não encontrado")
        return
    
    campo_login = pyautogui.locateOnScreen("last-name.png", confidence=0.8)
    if campo_login:
        time.sleep(1.5)
        pyautogui.click(campo_login) # se o campo_login for encontrado vai localizar a imagem
        pyautogui.typewrite(last_name) # depois vai escrever o usuario
    else:
        print("Campo de sobrenome não encontrado")
        return
    pyautogui.press("enter")




login_automatico("John", "Smith", "IT Solutions", "Analyst", "98 North Road", "jsmith@itsolutions.co.uk", "40716543298") 