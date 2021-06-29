from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http:\\localhost:9999/kitchensink.html")

button = driver.find_element_by_id('openwindow')
print(button.text)

input_1 = driver.find_element_by_name('cars')
print(input_1.tag_name)

legend = driver.find_element_by_xpath('/html/body/div[4]/div[1]/fieldset/legend')
print(legend.text)

driver.close()
