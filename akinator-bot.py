from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

name = input("Nome da pessoa: ")
desc = input("Descrição (menos de 50 caracteres): ")
if len(desc) >= 50:
    print("Descrição muito grande.")
    exit()

browser = webdriver.Firefox()

#browser.install_addon(
    #"/home/../.mozilla/firefox/gonwkrxi.default-release/extensions/uBlock0@raymondhill.net.xpi",
    #temporary=True,
#)
browser.get("https://pt.akinator.com")

try:
    button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "btn-play"))
    )
except Exception:
    browser.quit()

button.find_element(By.CSS_SELECTOR, "a").click()

while True:
    WebDriverWait(browser, 10).until(
        EC.invisibility_of_element_located((By.ID, "div-overlay"))
    )
    try:
        element = browser.find_element(By.ID, "a_yes").click()
    except:
        element = browser.find_element(By.ID, "a_propose_no").click()
        WebDriverWait(browser, 10).until(
            EC.invisibility_of_element_located((By.ID, "div-overlay"))
        )
        element = browser.find_element(By.ID, "a_continue_no").click()
        WebDriverWait(browser, 10).until(
            EC.invisibility_of_element_located((By.ID, "div-overlay"))
        )
        element = browser.find_element(By.ID, "not_in_list").click()
        WebDriverWait(browser, 10).until(
            EC.invisibility_of_element_located((By.ID, "div-overlay"))
        )
        element = browser.find_element(By.NAME, "name").send_keys(
            name + Keys.RETURN
        )
        WebDriverWait(browser, 10).until(
            EC.invisibility_of_element_located((By.ID, "div-overlay"))
        )
        element = browser.find_element(By.ID, "show_add_perso").click()
        WebDriverWait(browser, 10).until(
            EC.invisibility_of_element_located((By.ID, "div-overlay"))
        )
        element = browser.find_element(By.NAME, "name").send_keys(
            name + Keys.RETURN
        )
        element = browser.find_element(By.NAME, "desc").send_keys(
            desc + Keys.RETURN
        )
        WebDriverWait(browser, 10).until(
            EC.invisibility_of_element_located((By.ID, "div-overlay"))
        )
        button = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "btn-play"))
        )
        button.find_element(By.CSS_SELECTOR, "a").click()
