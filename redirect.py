


from selenium import webdriver
import math


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

window_before = browser.window_handles[0]

button = browser.find_element_by_css_selector("button.btn")
button.click()

window_after = browser.window_handles[1]
browser.switch_to.window(window_after)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_xpath("//*[@id='input_value']")
x = x_element.text
y = calc(x)

field = browser.find_element_by_xpath("//*[@id='answer']")
field.send_keys(y)

button = browser.find_element_by_css_selector("button.btn")
button.click()
