# from selenium import webdriver
#
# browser = webdriver.Chrome()
# link = "https://SunInJuly.github.io/execute_script.html"
# browser.get(link)
# button = browser.find_element_by_tag_name("button")
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# # browser.execute_script("window.scrollBy(0, 100);")
# button.click()
# assert True

# // javascript
# button = document.getElementsByTagName("button")[0];
# button.scrollIntoView();

from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_xpath("//*[@id='input_value']")
x = x_element.text
y = calc(x)

field = browser.find_element_by_xpath("//*[@id='answer']")
field.send_keys(y)

checkbox1 = browser.find_element_by_id("robotCheckbox")
browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox1)
checkbox1.click()

radio2 = browser.find_element_by_css_selector("[for='robotsRule']")
radio2.click()

button = browser.find_element_by_css_selector("button.btn")
button.click()