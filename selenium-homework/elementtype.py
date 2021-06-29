from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http:\\localhost:9999/trickyelements.html")

element1 = driver.find_elements_by_xpath('//*[@id="element1"]')
element2 = driver.find_elements_by_xpath('//*[@id="element2"]')
element3 = driver.find_elements_by_xpath('//*[@id="element3"]')
element4 = driver.find_elements_by_xpath('//*[@id="element4"]')
element5 = driver.find_elements_by_xpath('//*[@id="element5"]')

elements = [element1, element2, element3, element4, element5]


driver.close()