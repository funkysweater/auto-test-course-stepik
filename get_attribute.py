from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

human_radio = browser.find_element_by_id("humanRule")

human_checked = human_radio.get_attribute("checked")
print("value of human radio: ", human_checked)
# assert human_checked is not None, "Human radio is not selected by default"
assert human_checked == "true", "Human radio is not selected by default"

robots_radio = browser.find_element_by_id("robotsRule")
robots_checked = robots_radio.get_attribute("checked")
print("robot radio value is: ", robots_checked)
assert robots_checked is None

# time.sleep(1)
#
# checkbox1 = browser.find_element_by_id("robotCheckbox")
# checkbox1.click()
#
# radio2 = browser.find_element_by_css_selector("[for='robotsRule']")
# radio2.click()
#
# button = browser.find_element_by_css_selector("button.btn")
# button.click()

