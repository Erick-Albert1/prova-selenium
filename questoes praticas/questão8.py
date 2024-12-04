from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Iniciar o navegador
driver = webdriver.Chrome()

# Acessar o site do Selenium
driver.get("https://www.selenium.dev/")

# Navegar até a seção Downloads clicando no link correspondente
download_link = driver.find_element_by_link_text("Downloads")
download_link.click()

# Aguardar até que a página de Downloads esteja carregada
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

# Extrair o texto do cabeçalho principal (h1 ou h2) da página
header_text = driver.find_element_by_tag_name("h1").text
print("Cabeçalho principal:", header_text)

# Fechar o navegador
driver.quit()
