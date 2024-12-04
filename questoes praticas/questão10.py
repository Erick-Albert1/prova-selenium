from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Iniciar o navegador
driver = webdriver.Chrome()

# Acessar a página de login
driver.get("https://the-internet.herokuapp.com/login")

# Preencher o formulário de login
username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")
username.send_keys("tomsmith")
password.send_keys("SuperSecretPassword!")

# Clicar no botão de login
login_button = driver.find_element_by_css_selector("button[type='submit']")
login_button.click()

# Validar se o login foi bem-sucedido
try:
    # Esperar até que a mensagem de sucesso esteja presente na página
    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.flash.success"))
    )
    assert "You logged into a secure area!" in success_message.text
    print("Login bem-sucedido!")
except:
    print("Falha no login!")

# Fechar o navegador
driver.quit()
