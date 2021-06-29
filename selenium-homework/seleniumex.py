from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https:\\opera.hu")

# a létező menubar helyett nem létező menubars id-t keres
try:
    menu_button = driver.find_element_by_xpath('//*[@id="menubars"]/li[1]/a[1]')
    menu_button.click()
except:
    print('Valami nem okés!!!')
finally:
   driver.close()