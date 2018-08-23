#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import json
import os
import win32api
import win32con
import pyautogui
from win32api import GetSystemMetrics
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

option = webdriver.ChromeOptions()
option.add_argument(r"user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data\Profile 6")
browser = webdriver.Chrome(chrome_options=option)
#browser = webdriver.Firefox()
browser.set_page_load_timeout(15)
browser.set_script_timeout(15)
browser.maximize_window()

width = GetSystemMetrics(0)
heigth = GetSystemMetrics(1)

try:
    browser.get('https://www.amazon.com')
except TimeoutError as e:
    print(type(e))
    print("加载超时")
    pass
finally :
    try:
        browser.get('https://www.amazon.com')
    except TimeoutError as e:
        print(type(e))
        print("加载超时")
        pass
    finally:
        try:
            time.sleep(random.randint(3,6))
            browser.execute_script('window.stop()')
            input_box = browser.find_element_by_id('twotabsearchtextbox')
        except Exception as e:
            print(type(e))
            print("找不到输入框")
            pass
        finally :
                if input_box.is_displayed():
                    print("找到输入框")
                    browser.set_page_load_timeout(1)
                    browser.set_script_timeout(1)
                    for character in "echo dot":
                        try:
                            input_box.send_keys(character)
                            time.sleep(0.3)  # pause for 0.3 seconds
                        except Exception as e:
                            print(type(e))
                            try:
                                input_box.send_keys(character)
                                time.sleep(0.3)  # pause for 0.3 seconds
                            except Exception as e:
                                print(type(e))
                                pass
                            finally:
                                pass
                        finally:
                            pass
                    browser.set_page_load_timeout(15)
                    browser.set_script_timeout(15)
                    try:
                        browser.execute_script('window.stop()')
                        suggestions = browser.find_element_by_id('issDiv0')
                        print("first suggestion is " + suggestions.text)
                        try:
                            if suggestions.is_enabled():
                                suggestions.click()
                            else:
                                print("suggestions error")
                        except Exception as e:
                            print(type(e))
                            try:
                                input_box.send_keys(Keys.ENTER)
                            except Exception as e:
                                print(type(e))
                                pass
                            finally:
                                pass
                        finally :
                            pass
                    except Exception as e:
                        print(type(e))
                        pass
                    finally :
                            move_count = 0
                            while move_count < 3:
                                x = random.randint(0, int(width / 3))
                                y = random.randint(0, int(heigth / 3)) + 200
                                move_time = random.randint(1, 20) * 1000 / 10000
                                pyautogui.moveTo(x, y, move_time)
                                time.sleep(random.randint(2, 4))
                                move_count += 1
                            move_count = 0
                            pyautogui.moveTo(random.randint(10, 800), random.randint(100, 500))
                            while move_count < 10:
                                scroll_count = random.randint(300, 1200)
                                for i in range(scroll_count):
                                    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, -1)
                                time.sleep(random.randint(1, 3))
                                move_count += 1
                            try:
                                try:
                                    print("current_url is " + browser.current_url)
                                except:
                                    pass
                                finally:
                                    pass
                            finally:
                                browser.quit()

                else:
                        browser.quit()
