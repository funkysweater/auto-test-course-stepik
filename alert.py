# alert('Hello!');


# alert = browser.switch_to.alert
# alert.accept()
#
# alert = browser.switch_to.alert
# alert_text = alert.text
#
# confirm = browser.switch_to.alert
# confirm.accept()
#
# confirm.dismiss()
#
#
# prompt = browser.switch_to.alert
# prompt.send_keys("My answer")
# prompt.accept()

# pip install pyperclip
# alert = browser.switch_to.alert
# alert_text = alert.text
# addToClipBoard = alert_text.split(': ')[-1]
# pyperclip.copy(addToClipBoard)

from selenium import webdriver
import math
# import pyperclip

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_css_selector("button.btn")
button.click()

confirm = browser.switch_to.alert
confirm.accept()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_xpath("//*[@id='input_value']")
x = x_element.text
y = calc(x)

field = browser.find_element_by_xpath("//*[@id='answer']")
field.send_keys(y)

button = browser.find_element_by_css_selector("button.btn")
button.click()

# alert = browser.switch_to.alert
# alert_text = alert.text
# addToClipBoard = alert_text.split(': ')[-1]
# pyperclip.copy(addToClipBoard)