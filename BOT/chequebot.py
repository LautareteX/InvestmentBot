from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

url = "https://micheque.uy/login"
driver = webdriver.Chrome() # Cambia Chrome por tu navegador de confianza
driver.get(url)

# Coloca tus credenciales
email= "youremail@email.com"
password = "****"

message = 'NUEVA OPORTUNIDAD'

# Iniciar sesion
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
web_pass = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
username.clear()
web_pass.clear()
username.send_keys("")
web_pass.send_keys("")

# Clic en iniciar sesion
button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-home.btn-home-small.btn-primary")))
button.click()

# Esperar a que se cargue la pagina despues de iniciar sesion
time.sleep(5)

# Verificacion periodica del boton
while True:
    try:
        # Verifica si el boton esta vvisible
        boton_nueva_oportunidad = driver.find_element(By.CSS_SELECTOR, "button.btn-refresh.btn.btn-default.btn-market")
        if boton_nueva_oportunidad.is_displayed():
            print("NUEVA OPORTUNIDAD")
        else:
            print("Sin novedad")
    except Exception as e:
        # El boton no esta presente en el DOM
        print("Sin novedad")

    # Verificacion cada 30 seg
    time.sleep(30)
