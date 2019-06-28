from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_class_name('first:required')
input1.send_keys("test1")
input2 = browser.find_element_by_class_name('second:required')
input2.send_keys("test2")
input3 = browser.find_element_by_class_name('third:required')
input3.send_keys("test3")

button = browser.find_element_by_css_selector("button.btn")
button.click()

time.sleep(1)

welcome_text_elt = browser.find_element_by_tag_name("h1")

welcome_text = welcome_text_elt.text


assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text

