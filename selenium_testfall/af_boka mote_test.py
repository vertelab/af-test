#!/usr/bin/python
# coding: utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from datetime import datetime
from datetime import timedelta
from faker import Faker

# Slumpar dag
faker = Faker()
date = faker.future_datetime(end_date='+30d', tzinfo=None)
day = date.strftime("%Y-%m-%d %H:%M:%S")

# Startar webdriver
browser = webdriver.Chrome()
browser.maximize_window()
wait = WebDriverWait(browser, 20)

# Credentials
user_name = "demo"
password = "demo"
kontakt = "Admin"

# Går in på databasen AFtema och loggar in
browser.get('https://fossa.vertel.se//web?db=AFtema')
element = browser.find_element_by_id("login")
element.send_keys(user_name)
element = browser.find_element_by_id("password")
element.send_keys(password)
element.send_keys(Keys.RETURN)
print('Inloggad')

# Går till kontakter
browser.get('https://fossa.vertel.se/web?db=AFtema#action=126&model=res.partner&view_type=kanban&menu_id=96')
print('Går till kontakter')

# Söker kontakt
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@class='o_searchview_input']")))
element.click()
element.send_keys(kontakt)
element.send_keys(Keys.RETURN)
print('Söker kontakt')

# Nästa sida med pilarna
# wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='fa fa-chevron-right btn btn-secondary o_pager_next']"))).click()
# print('Nästa sida med pilarna')

# Öppna kontaktkort
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='oe_kanban_global_click o_kanban_record_has_image_fill o_res_partner_kanban o_kanban_record']"))).click()
print('Öppnar kontaktkort')

# Går till listvy i kalender
browser.get('https://fossa.vertel.se/web?db=AFtema#action=124&model=calendar.event&view_type=list&menu_id=92')
print('Går till listvy i kalender')

# Skapar nytt möte
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary o_list_button_add']"))).click()
print('Skapar nytt möte')

# Namnger mötet
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='name']")))
element.send_keys("Testar att boka")
print('Namnger möte')

# Väljer slumpad dag för mötet
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='start_datetime']")))
element.click()
element.clear()
element.send_keys(day)
print('Väljer slumpad dag')

# Väljer hur länge mötet är
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='duration']")))
element.clear()
element.send_keys("02:00")
print('Väljer mötets längd')

# Sparar mötet
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary o_form_button_save']"))).click()
print('Sparar möte')

# Loggar ut
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='dropdown-toggle']"))).click()
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-menu='logout']"))).click()
print('Loggar ut')

# Stänger
browser.close()