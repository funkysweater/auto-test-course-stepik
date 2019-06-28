from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(link)

name = browser.find_element_by_xpath("//input[@placeholder='Введите имя']")
name.send_keys("Ivan")
lastName = browser.find_element_by_xpath("//input[@placeholder='Введите фамилию']")
lastName.send_keys("Petrov")
email = browser.find_element_by_xpath("//input[@placeholder='Введите Email']")
email.send_keys("example@stepik.org")

button = browser.find_element_by_css_selector("button.btn")
button.click()

time.sleep(1)

welcome_text_elt = browser.find_element_by_tag_name("h1")
welcome_text = welcome_text_elt.text

assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text