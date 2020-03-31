#!/usr/bin/python
# coding: utf-8

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from xvfbwrapper import Xvfb
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from datetime import datetime, timedelta
from faker import Faker

# Slumpar dag
faker = Faker()
date = faker.future_datetime(end_date='+30d', tzinfo=None)
day = date.strftime("%Y-%m-%d %H:%M:%S")

# Startar wrapper
# vdisplay = Xvfb()
# vdisplay.start()

# Startar webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
browser = webdriver.Chrome(chrome_options=chrome_options)
# browser.maximize_window()
wait = WebDriverWait(browser, 30)

# Credentials
user_name = "demo"
password = "demo"
kontakt = "Admin"

# Startar timer
start = time.time()
print("Startar timer")

# Går in på databasen AFtema och loggar in
print('Loggar in')
browser.get('https://fossa.vertel.se//web?db=AFtema')
element = browser.find_element_by_id("login")
element.send_keys(user_name)
element = browser.find_element_by_id("password")
element.send_keys(password)
element.send_keys(Keys.RETURN)

# Går till kontakter
print('Går till kontakter')
browser.get('https://fossa.vertel.se/web?db=AFtema#action=126&model=res.partner&view_type=kanban&menu_id=96')

# Söker kontakt
print('Söker kontakt')
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@class='o_searchview_input']")))
element.click()
element.send_keys(kontakt)
element.send_keys(Keys.RETURN)

# Nästa sida med pilarna
# wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='fa fa-chevron-right btn btn-secondary o_pager_next']"))).click()
# print('Nästa sida med pilarna')

# Öppna kontaktkort
print('Öppnar kontaktkort')
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='oe_kanban_global_click o_kanban_record_has_image_fill o_res_partner_kanban o_kanban_record']"))).click()

# Går till listvy i kalender
print('Går till listvy i kalender')
browser.get('https://fossa.vertel.se/web?db=AFtema#action=124&model=calendar.event&view_type=list&menu_id=92')

# Skapar nytt möte
print('Skapar nytt möte')
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary o_list_button_add']"))).click()

# Namnger mötet
print('Namnger möte')
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='name']")))
element.send_keys("Testar att boka")

# Väljer slumpad dag för mötet
print('Väljer slumpad dag')
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='start_datetime']")))
element.click()
element.clear()
element.send_keys(day)

# Väljer hur länge mötet är
print('Väljer mötets längd')
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='duration']")))
element.clear()
element.send_keys("02:00")

# Tar screenshot på bokat möte
print("Tar screenshot")
browser.get_screenshot_as_file("capture.png")

# Sparar mötet
print('Sparar möte')
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary o_form_button_save']"))).click()

# Loggar ut
print('Loggar ut')
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='dropdown-toggle']"))).click()
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-menu='logout']"))).click()

# Avslutar timer
print("Avslutar timer")
end = time.time()

test_tid = end - start

print("Testtid: %s" % test_tid)

# Stänger
browser.close()

# Avslutar wrapper
# vdisplay.stop()



