
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

n1 = browser.find_element_by_id("num1")
x = n1.text
n2= browser.find_element_by_id("num2")
y = n2.text

z = str(int(x) + int(y))
print (z)
str(z)

# option1  = browser.find_element_by_css_selector("[value='result']")

from selenium.webdriver.support.ui import Select
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(z)

button = browser.find_element_by_css_selector("button.btn")
button.click()