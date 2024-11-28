from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome() # abre o google
driver.get("file://C:/Users/74992/RPA-fundaments/chrome-driver/index.html") # abre um site qualquer pela sua url
time.sleep(2) # da um tempo de 2 segundos
campo_usuario = driver.find_element(By.ID, "usuario") # acha o elemento pelo seu id 
campo_senha = driver.find_element(By.ID, "senha") # acha o elemento pelo seu id 
botao_login = driver.find_element(By.XPATH, "//*[@id='loginForm']/button") # botão localizado pelo seu xpath para achar e so ir no f12 na pagina e apertar encima do botao com botao direito e copiar o xpath

campo_usuario.send_keys("ALUNOS") # preenche o campo com o id usuario com ALUNOS
campo_senha.send_keys("SUPERDEV") # preenche o campo com o id senha com SUPERDEV
botao_login.click() # clica no botao de login
time.sleep(4) # tempo de dois segundos

