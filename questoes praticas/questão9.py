from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Iniciar o navegador
driver = webdriver.Chrome()

# Acessar um site de exemplo que gera um alerta
driver.get("https://www.exemplo.com/gera_alerta")

# Esperar até que o alerta esteja presente
WebDriverWait(driver, 10).until(EC.alert_is_present())

# Alternar para o alerta e fechá-lo
alerta = driver.switch_to.alert
alerta.accept()  # Isso clica no botão "OK" do alerta

# Fechar o navegador
driver.quit()
