from selenium import webdriver
from selenium.webdriver.common.by import By
import time

navegador = webdriver.Chrome()

navegador.maximize_window()

navegador.get("https://app.santanderopenacademy.com/pt-BR/course/introduction_to_python_programming")

time.sleep(5)

# Entra no primeiro Shadow DOM
header = navegador.find_element(By.CSS_SELECTOR, "body > soa-web-root > div > soa-web-header > soa-header")
shadow1 = header.shadow_root

# Entra no segundo Shadow DOM
desktop = shadow1.find_element(By.CSS_SELECTOR, "soa-header-desktop")
shadow2 = desktop.shadow_root

# Procura o botão
botaoAcessar = shadow2.find_element(By.ID, "access")
botaoAcessar.click()

time.sleep(10)