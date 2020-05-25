#!/usr/bin/python
# coding: utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import odooselenium

# Startar webbläsaren
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 20)

# Uppgifter
user_name = "admin"
password = ""
contact = "Malin Larsson"

# Väljer databas
driver.get("https://fossa.vertel.se/web/database/selector")
link = driver.find_element_by_link_text("ACRMTEST03")
link.click()

# Loggar in
element = driver.find_element_by_id("login")
element.send_keys(user_name)
element = driver.find_element_by_id("password")
element.send_keys(password)
element.send_keys(Keys.RETURN)
print('Inloggad')

# Går in på kontakter
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//i[@class='fa fa-th-large']")))
element.click()
element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Kontakter")))
element.click()
time.sleep(1)
print("Kontakter")

# Söker efter kontakt
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@class='o_searchview_input']")))
element.click()
element.send_keys(contact)
element.send_keys(Keys.RETURN)
time.sleep(2)
print("Söker efter kontakt")

# Går in på kontaktkortet
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='oe_kanban_global_click o_kanban_record_has_image_fill o_res_partner_kanban o_kanban_record']")))
element.click()
print('Öppnar kontaktkort')

# Klickar på redigera
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary o_form_button_edit']")))
element.click()
print("Klickar på redigera")

# Klickar på Daily notes
element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Daily Notes")))
element.click()
print("Klickar på fliken Daily Notes")

# Lägger till rad
element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Lägg till rad")))
element.click()
print("Lägg till rad")

# Skriver Titel
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='name']")))
element.send_keys("Möte")
print("Titel")

# Skriver Anteckning

# Skriver in datum

# Väljer typ

# Väljer kontor

# Klickar på spara 
#element = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary o_form_button_save']")))
#element.click()
#print("Klickar på spara")

# Stänger fönster
#driver.close()