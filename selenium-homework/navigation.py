from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http:\\localhost:9999/general.html")

anchors = driver.find_elements_by_xpath('//a')

for a in anchors:
    a.click()

    print(driver.current_url)

driver.close()