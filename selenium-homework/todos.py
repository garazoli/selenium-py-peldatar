from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http:\\localhost:9999/todo.html")

todos = driver.find_element_by_xpath('/html/body/div/div/div/ul')
print(todos.text)

driver.close()