import tkinter as tk
import traceback
import time

import driver
import ui

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains

def instaSend(id, msg):
    try:
        # 발송 start
        link = WebDriverWait(driver.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[aria-label^="Direct"]'))
        )
        href = link.get_attribute('href')
        driver.driver.get(href)
        
        # loop 스타트
        new_message_icon = WebDriverWait(driver.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'svg[aria-label="새로운 메시지"]'))
        )
        new_message_icon.click()
        
        userSearchBox = WebDriverWait(driver.driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'queryBox'))
        )
        userSearchBox.send_keys(id)
        
        userCheckBox = WebDriverWait(driver.driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'ContactSearchResultCheckbox'))
        )
        if userCheckBox is not None:
            userCheckBox.click()
            chat_div = WebDriverWait(driver.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[text()='채팅']"))
            )
            chat_div.click()
            editable_div = WebDriverWait(driver.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@aria-label='메시지' and @contenteditable='true']"))
            )
            actions = ActionChains(driver.driver)
            actions.move_to_element(editable_div)
            actions.click()
            for m in msg:
#                editable_div.send_keys(m)
                actions.send_keys(m).perform()
                actions.key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT).perform()
            editable_div.send_keys(Keys.ENTER)
    except Exception as e:
        print(f"Error: {e}")
        traceback.print_exc()

def instaCloseAlim():
    try:
        alim_box = WebDriverWait(driver.driver, 1).until(
            EC.presence_of_element_located((By.CLASS_NAME, "_a9_1"))
        )
        if alim_box is not None:
            alim_box.click()
    except Exception as e:
        print(f"Error: {e}")
        traceback.print_exc()

def instaLogin(id, password, root):
    try:
        ui.button.config(state=tk.DISABLED)
        s = Service(executable_path=driver.driver_path)
        options = Options()
        options.add_experimental_option("detach", True)
        driver.driver = webdriver.Chrome(service=s, options=options)
        monitor = driver.BrowserMonitor(driver.driver)
        monitor.start()

        driver.driver.get('https://www.instagram.com/')

        usernameBox = WebDriverWait(driver.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        passwordBox = driver.driver.find_element(By.NAME, 'password')
        
        # usernameBox.send_keys("dhn_kakao")
        # passwordBox.send_keys("indhn^^4556")
        usernameBox.send_keys(id)
        passwordBox.send_keys(password)
        
        passwordBox.submit()
        time.sleep(3)
        instaCloseAlim()
        root.after(0, lambda: ui.button2.config(state=tk.NORMAL))
        
    except Exception as e:
        print(f"Error: {e}")
        traceback.print_exc()