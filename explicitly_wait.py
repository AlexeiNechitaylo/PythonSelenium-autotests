from selenium import webdriver
import math

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))
	
url = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(url)

price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '10000 RUR'))
print("I found when price equals 10000")

button = browser.find_element_by_class_name("btn-primary")
button.click()

element_x = browser.find_element_by_id("input_value")
x = element_x.text
y = calc(x)

field = browser.find_element_by_class_name("form-control")
field.send_keys(y)

submit = browser.find_element_by_id("solve")
submit.click()
#
