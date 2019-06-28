from selenium import webdriver

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)
browser.execute_script("alert('Robots at work');")


# browser.execute_script("document.title='Script executing';")
# browser.execute_script('document.title="Script executing";')
# browser.execute_script("document.title='Script executing';alert('Robots at work');")


# element = browser.execute_script('document.getElementsByName("name")')
#
# Так же есть конструкции:
# getElementById
# getElementsByTagName
# getElementsByClassName
# querySelector - для CSS
# querySelectorAll - для CSS (находит все совпадения)
#
# evaluate - для XPATH.