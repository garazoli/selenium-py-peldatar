import csv

from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    driver.get("http://localhost:9999/another_form.html")


    def find_and_clear_element_by_id(id):
        element = driver.find_element_by_id(id)
        element.clear()
        return element


    with open('table_in.csv') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)
        for row in csvreader:
            find_and_clear_element_by_id('fullname').send_keys(row[0])
            find_and_clear_element_by_id('email').send_keys(row[1])
            find_and_clear_element_by_id('dob').send_keys(row[2])
            find_and_clear_element_by_id('phone').send_keys(row[3])
            driver.find_element_by_id('submit').click()

finally:
    pass
    # driver.close()
