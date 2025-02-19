from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
import time
from text_create import list_item


CHROME_WEBDRIVER  = "chromedriver.exe"

options = webdriver.ChromeOptions()
profile = "C:/Users/Anil/AppData/Local/Google/Chrome/User Data/Default"

options.add_argument(f"user-data-dir=C:/Users/Anil/AppData/Local/Google/Chrome/User Data")  # Replace with your Chrome profile path
options.add_argument(f"profile-directory=Default")

service = webdriver.ChromeService(executable_path=CHROME_WEBDRIVER)
driver = webdriver.Chrome(options=options, service=service)
driver.get("https://www.bing.com")
time.sleep(15)


for item in list_item:
    search = driver.find_element(by='name',value='q')
    search.clear()
    search.send_keys(item)
    time.sleep(1)
    search.send_keys(Keys.ENTER)
    time.sleep(6)