from selenium import webdriver
import time
import math
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

browser.find_element_by_xpath("//input[@placeholder='Введите имя']").send_keys("Laura")
browser.find_element_by_xpath("//input[@placeholder='Введите фамилию']").send_keys("Palmer")
browser.find_element_by_xpath("//input[@placeholder='Введите Email']").send_keys("lp@blacklodge.me")

upload = browser.find_element_by_id("file")
# upload.click()

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла

print(os.path.abspath(__file__))

file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
upload.send_keys(file_path)

print(os.path.abspath(os.path.dirname(__file__)))


button = browser.find_element_by_css_selector("button.btn")
button.click()
