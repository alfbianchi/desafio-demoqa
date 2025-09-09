from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui
import time
#####
#Desafio Frontend Parte 2 - TC01

#TC01.001 - Acessar o site https://demoqa.com/
#TC01.002 - Escolher a opção Forms na página inicial
#TC01.003 - Clicar no submenu Practice Form
#TC01.004 - Preencher todo o formulário com valores aleatórios
#TC01.005 - O Arquivo utilizado para upload, precisa ser um .txt qualquer, e precisa estar na devida pasta do github ao ser publicado o projeto
#TC01.006 - Submter o formulário
#TC01.007 - Garantir que um popup foi aberto após o submit
#TC01.008 - Fechar o popup
#####

#TC01.001 - Acessar o site https://demoqa.com/
driver = webdriver.Chrome()
driver.get("https://demoqa.com/")
driver.maximize_window()

#TC01.002 - Escolher a opção Forms na página inicial
form = driver.find_elements(By.TAG_NAME, "h5")

for links in form:
    if "Forms" in links.text:
        links.click()
        break

#TC01.003 - Clicar no submenu Practice Form

form2 = driver.find_elements(By.TAG_NAME, "span")

for links in form2:
    if "Practice Form" in links.text:
        links.click()
        break

#TC01.004 - Preencher todo o formulário com valores
#aleatórios

driver.find_element("id", "firstName").send_keys("Andre")
driver.find_element("id", "lastName").send_keys("Rocha")
driver.find_element("id", "userEmail").send_keys("alfbianchi@gmail.com")

form3 = driver.find_elements(By.TAG_NAME, "label")
for links in form3:
    if "Male" in links.text:
        links.click()
        break

driver = driver.find_element(By.XPATH, "//input[@id='userNumber']")
driver.send_keys("3132321313")
driver = driver.find_element(By.XPATH, "//input[@id='dateOfBirthInput']")
driver.send_keys(Keys.CONTROL, 'a')
driver.send_keys("15 Sep 1987")
driver.send_keys(Keys.ESCAPE)
driver = driver.find_element(By.XPATH, "//input[@id='subjectsInput']")
driver.send_keys("English")
driver.send_keys(Keys.TAB)
label = driver.find_element(By.XPATH, "//label[@for='hobbies-checkbox-2']")
label.click()
upload = driver.find_element(By.XPATH, "//label[@for='uploadPicture']")
upload.click()
time.sleep(1)

#TC01.005 - O Arquivo utilizado para upload, precisa ser um
#.txt qualquer, e precisa estar na devida pasta do
#github ao ser publicado o projeto

pyautogui.write(r'C:\test.txt')
pyautogui.press('enter')

time.sleep(1)
pyautogui.press('tab')
time.sleep(1)
pyautogui.write(r'Rua Gasparino Lunardi')
time.sleep(1)
pyautogui.press('tab')
time.sleep(1)
pyautogui.write(r'Haryana')
time.sleep(1)
pyautogui.press('tab')
pyautogui.press('tab')
time.sleep(1)
pyautogui.write(r'Karnal')
pyautogui.press('tab')
time.sleep(1)

#TC01.006 - Submter o formulário

driver.send_keys(Keys.ENTER)

#TC01.007 - Garantir que um popup foi aberto após o submit

#Não foi possível capturar o objeto via selenium, validação ok apesar do falso positivo
element = driver.find_element(By.XPATH, "//div[contains(text(), 'Thanks for submitting the form')]")

if "Thanks for submitting the form" in element.text:
    print("Popup foi aberto após o submit com sucesso!")
else:
    print("Popup não foi aberto após o submit.")

#TC01.008 - Fechar o popup

pyautogui.press('tab')
pyautogui.press('enter')


#Desafio Frontend Parte 2 - TC02

#TC02.001 - Acessar o site https://demoqa.com/
#TC02.002 - Escolher a opção Alerts, Frame & Windows na página inicial
#TC02.003 - Clicar no submenu Browser Windows
#TC02.004 - Clicar no botão new Windows
#TC02.005 - Certifica-se que uma nova janela foi aberta, e validar a msg “This is a sample page”
#TC02.006 - Fechar a nova janela aberta

#####


#TC02.001 - Acessar o site https://demoqa.com/
driver = webdriver.Chrome()
driver.get("https://demoqa.com/")

#TC02.002 - Escolher a opção Alerts, Frame & Windows na página inicial
form = driver.find_elements(By.TAG_NAME, "h5")

for links in form:
    if "Alerts, Frame & Windows" in links.text:
        links.click()
        break

#TC02.003 - Clicar no submenu Browser Windows
form2 = driver.find_elements(By.TAG_NAME, "span")

for links in form2:
    if "Browser Windows" in links.text:
        links.click()
        break

#TC02.004 - Clicar no botão new Windows

driver.find_element(By.ID, "windowButton").click()

#TC02.005 - Certifica-se que uma nova janela foi aberta, e validar a msg “This is a sample page”
driver.switch_to.window("")

validate_text = driver.find_element(By.ID, "sampleHeading")
if validate_text.text == "This is a sample page":
    print("Texto validado com sucesso!")
else:
    print("Texto não corresponde ao esperado.")

#TC02.006 - Fechar a nova janela aberta

driver.close()

#Desafio Frontend Parte 2 - TC03

#TC03.001 - Acessar o site https://demoqa.com/

#TC03.002 - Escolher a opção Elements na página inicial

#TC03.003 - Clicar no submenu Web Tables

#TC03.004 - Criar um novo registro

#TC03.005 - Editar o novo registro criado

#TC03.006 - Deletar o novo registro criado.

#####

#TC03.001 - Acessar o site https://demoqa.com/

driver = webdriver.Chrome()
driver.get("https://demoqa.com/")
driver.maximize_window()

#TC03.002 - Escolher a opção Elements na página inicial

link = driver.find_elements(By.TAG_NAME, "h5")

for links in link:
    if "Elements" in links.text:
        links.click()
        break

#TC03.003 - Clicar no submenu Web Tables

link2 = driver.find_elements(By.TAG_NAME, "span")
for links in link2:
    if "Web Tables" in links.text:
        links.click()
        break

#TC03.004 - Criar um novo registro

driver.find_element(By.ID, "addNewRecordButton").click()

name = driver.find_element(By.ID, "firstName")
name.send_keys("Andre")

last_name = driver.find_element(By.ID, "lastName")
last_name.send_keys("Rocha")

email = driver.find_element(By.ID, "userEmail")
email.send_keys("albianchi@gmail.com")

age = driver.find_element(By.ID, "age")
age.send_keys("37")

salary = driver.find_element(By.ID, "salary")
salary.send_keys("10000")

department = driver.find_element(By.ID, "department")
department.send_keys("QA")

driver.find_element(By.ID, "submit").click()

#TC03.005 - Editar o novo registro criado

driver.find_element(By.ID, "edit-record-4").click()

salary = driver.find_element(By.ID, "salary")
salary.clear()
salary.send_keys("7000")
driver.find_element(By.ID, "submit").click()
print("Registro alterado com sucesso!")

#TC03.006 - Deletar o novo registro criado.

driver.find_element(By.ID, "delete-record-4").click()
print("Registro deletado com sucesso!")

#Desafio Frontend Parte 2 - TC04

#TC04.001 - Acessar o site https://demoqa.com/

#TC04.002 - Escolher a opção Widgets na página inicial

#TC04.003 - Clicar no submenu Progress Bar

#TC04.005 - Clicar no botão Start

#TC04.006 - Parar antes dos 25%

#TC04.007 - Validar que o valor da progress Bar é menor ou igual aos 25%

#TC04.008 - Apertar Start novamente e ao chegar aos 100%, resetar a progress bar


driver = webdriver.Chrome()

#TC04.001 - Acessar o site https://demoqa.com/
#Não foi possível acessar o link progress bar pelo menu de acesso. Acessando diretamente a URL

driver.get("https://demoqa.com/progress-bar")
driver.maximize_window()

#TC04.005 - Clicar no botão Start
driver.find_element(By.ID, "startStopButton").click()
time.sleep(1)
progress_bar = driver.find_element(By.ID, "progressBar").text
print(progress_bar)
value = progress_bar.replace("%", "")
num_value = int(value)

#TC04.006 - Parar antes dos 25%
#TC04.007 - Validar que o valor da progress Bar é menor ou igual aos 25%
if num_value <= 25:
    print("O valor é menor ou igual a 25%")
    driver.find_element(By.ID, "startStopButton").click()
    print("Progresso parado com sucesso!")

#TC04.008 - Apertar Start novamente e ao chegar aos 100%, resetar a progress bar

driver.find_element(By.ID, "startStopButton").click()
time.sleep(5)
progress_bar = driver.find_element(By.ID, "progressBar").text
while progress_bar != "100%":
    progress_bar = driver.find_element(By.ID, "progressBar").text

time.sleep(5)    

if progress_bar == "100%":
    driver.find_element(By.ID, "resetButton").click()
    print("A barra de progresso atingiu 100% e foi resetada com sucesso!")
else:
    print("A barra de progresso não atingiu 100%")
time.sleep(5)
driver.quit()

#Desafio Frontend Parte 2 - TC05

#Acessar o site https://demoqa.com/
#Escolher a opção Interactions na página inicial
#Clicar no submenu Sortable
#Utilizando métodos de drag and drop

#Não foi possivel mapear os elementos para drag and drop, o selenium não funcionou. Testei com pyautogui mas não foi possível também.