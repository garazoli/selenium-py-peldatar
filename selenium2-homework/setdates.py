from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime, timezone
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://localhost:9999/forms.html")

nowutc = datetime.now(timezone.utc)

time.sleep(1)  # Csak hogy lássuk, mi történik
driver.find_element_by_id('example-input-date').send_keys(nowutc.strftime("00%Y/%m/%d"))
time.sleep(1)
driver.find_element_by_id('example-input-date-time').send_keys(nowutc.strftime("%Y.%m.%d %H:%M:%S:%f"))
time.sleep(1)
driver.find_element_by_id('example-input-date-time-local').send_keys(nowutc.strftime("00%Y/%m/%d%H:%M"))
time.sleep(1)
driver.find_element_by_id('example-input-month').send_keys(nowutc.strftime("%Y"))
time.sleep(1)
driver.find_element_by_id('example-input-month').send_keys(Keys.TAB)
time.sleep(1)
driver.find_element_by_id('example-input-month').send_keys(nowutc.strftime("%B"))
time.sleep(1)
driver.find_element_by_id('example-input-week').send_keys(nowutc.strftime("%W"))
time.sleep(1)
driver.find_element_by_id('example-input-week').send_keys(nowutc.strftime("%Y"))
time.sleep(1)
driver.find_element_by_id('example-input-time').send_keys(nowutc.strftime("%H%M"))

time.sleep(5)

driver.close()
