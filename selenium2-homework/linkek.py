from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    driver.get("http://localhost:9999/")
    links = driver.find_elements_by_xpath("//a")
    for link in links:
        with open('linkek.txt', 'a') as linkek:
            linkek.write(str(link.get_attribute("href"))+'\n')
        print(link.get_attribute("href"))

    len_links = len(links)
    print(f"Linkek száma: {len_links}")

finally:
    driver.close()
