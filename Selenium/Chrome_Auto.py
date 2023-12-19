from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.chrome()
driver.get("http://10.122.66.165:9000/")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.REYURN)
assert "No results found." not in driver.page_source