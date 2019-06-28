
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

chest = browser.find_element_by_css_selector("img")

attr = chest.get_attribute("valuex")
# human_checked = human_radio.get_attribute("checked")
print("valuex")
# assert human_checked is not None, "Human radio is not selected by default"
# assert human_checked == "true", "Human radio is not selected by default"

x = attr
y = calc(x)

field = browser.find_element_by_xpath("//*[@id='answer']")
field.send_keys(y)

checkbox1 = browser.find_element_by_id("robotCheckbox")
checkbox1.click()

radio2 = browser.find_element_by_id("robotsRule")
radio2.click()

button = browser.find_element_by_css_selector("button.btn")
button.click()

