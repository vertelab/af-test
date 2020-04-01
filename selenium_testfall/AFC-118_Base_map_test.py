#!/usr/bin/python
# coding: utf-8

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from datetime import datetime, timedelta

# Startar webdriver
chrome_options = Options()
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.maximize_window()
wait = WebDriverWait(browser, 20)

# Credentials
db = "http://odoo12:8069///web?db=AFtest"
user_name = "admin"
password = "admin"

# Startar timer
start = time.time()

# Går in på databasen AFtest och loggar in
print('Loggar in')
browser.get(db)
element = browser.find_element_by_id("login")
element.send_keys(user_name)
element = browser.find_element_by_id("password")
element.send_keys(password)
element.send_keys(Keys.RETURN)

# Aktiverar utvecklingsläge
print('Aktiverar utvecklingsläge')
wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='oe_topbar_name']"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-menu='debug']"))).click()

# Går till databas struktur Fields project.agile.jira.config
print('Går till databas struktur Fields project.agile.jira.config')
browser.get('http://odoo12:8069/web?debug=1#id=4454&action=16&model=ir.model.fields&view_type=form&menu_id=4')

# # Går in på flik Mapping
print('Går in på flik Mapping')
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Mapping']"))).click()

#  Trycker på redigera knapp
print('Trycker på redigera knapp')
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary o_form_button_edit']"))).click()

# # Väljer hur länge mötet är
print('Fyller i fält')
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='map_system']")))
element.clear()
element.send_keys("teleopti")
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='map_table']")))
element.clear()
element.send_keys("schedule")
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='map_field']")))
element.clear()
element.send_keys("start_date")
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='map_type']")))
element.clear()
element.send_keys("DateTime")
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='map_comment']")))
element.clear()
element.send_keys("Automatiskt testfall")

# Sparar
print('Sparar')
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary o_form_button_save']"))).click()

# Loggar ut
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='dropdown-toggle']"))).click()
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-menu='logout']"))).click()
print('Loggar ut')

# Avslutar timer
end = time.time()

test_tid = end - start

print("Testtid: %s" % test_tid)

# Stänger
browser.close()



