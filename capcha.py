from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_xpath("//*[@id='input_value']")
x = x_element.text
y = calc(x)

field = browser.find_element_by_xpath("//*[@id='answer']")
field.send_keys(y)

time.sleep(1)

checkbox1 = browser.find_element_by_id("robotCheckbox")
checkbox1.click()

radio2 = browser.find_element_by_css_selector("[for='robotsRule']")
radio2.click()

button = browser.find_element_by_css_selector("button.btn")
button.click()


