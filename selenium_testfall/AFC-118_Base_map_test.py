#!/usr/bin/python
# coding: utf-8

from selenium import webdriver
import os
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
user_name = "demo"
password = "demo"

# Startar timer
start = time.time()

# Går in på databasen AFtema och loggar in
browser.get('https://fossa.vertel.se//web?db=ACRMTEST03')
element = browser.find_element_by_id("login")
element.send_keys(user_name)
element = browser.find_element_by_id("password")
element.send_keys(password)
element.send_keys(Keys.RETURN)
print('Inloggad')

# Aktiverar utvecklingsläge
print('Aktiverar utvecklingsläge')
browser.get('https://fossa.vertel.se/web?debug')

# Går in på inställningar
print('Går in på inställningar')
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='full']"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-menu-xmlid='base.menu_administration']"))).click()

# # Går in på inställningar
print('Går in på inställningar')
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-display='static']"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-menu-xmlid='base.menu_administration']"))).click()


# Går till databas struktur Fields calendar.contacts
print('Går till databas struktur Fields calendar.contacts')
browser.get('https://fossa.vertel.se/web?debug#id=2331&action=16&model=ir.model.fields&view_type=form&menu_id=4')

# Går in på flik Mapping
print('Går in på flik Mapping')
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Mapping']"))).click()

#  Trycker på redigera knapp
print('Trycker på redigera knapp')
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary o_form_button_edit']"))).click()

# Fyller i fält
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

# # Sparar
print('Sparar')
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary o_form_button_save']"))).click()

# # Loggar ut
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='dropdown-toggle']"))).click()
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-menu='logout']"))).click()
print('Loggar ut')

# # Avslutar timer
end = time.time()

test_tid = end - start

print("Testtid: %s" % test_tid)

# Stänger
browser.close()



