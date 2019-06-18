from selenium import webdriver
import math


def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_css_selector('button.btn')
button.click()

alert = browser.switch_to.alert
alert.accept()


x_element = browser.find_element_by_id('input_value')
x = x_element.text

y = calc(int(x))

answer_element = browser.find_element_by_id('answer')
answer_element.send_keys(str(y))

button = browser.find_element_by_css_selector('button.btn')
button.click()