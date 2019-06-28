from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

book = browser.find_element_by_id("book")

button = WebDriverWait(browser, 12).until(
    (EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR"))
    )
print ("finally")
button = browser.find_element_by_id("book")
button.click()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_xpath("//*[@id='input_value']")
x = x_element.text
y = calc(x)

field = browser.find_element_by_xpath("//*[@id='answer']")
field.send_keys(y)

button = browser.find_element_by_id("solve")
button.click()