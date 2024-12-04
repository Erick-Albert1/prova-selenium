from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Iniciar o navegador
driver = webdriver.Chrome()

# Acessar o site do Google
driver.get("https://www.google.com")

# Procurar pela barra de pesquisa
search_bar = driver.find_element_by_name("q")

# Digitar a palavra "Python Selenium" e pressionar Enter
search_bar.send_keys("Python Selenium")
search_bar.send_keys(Keys.RETURN)

# Fechar o navegador
driver.quit()
