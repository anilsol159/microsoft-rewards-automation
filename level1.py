from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from text_create import list_item


CHROME_WEBDRIVER  = "chromedriver.exe"

options = webdriver.ChromeOptions()
profile = "C:/Users/Anil/AppData/Local/Google/Chrome/User Data/"

options.add_argument(f"user-data-dir=C:/Users/Anil/AppData/Local/Google/Chrome/User Data")  # Replace with your Chrome profile path
options.add_argument('--disable-infobars')

options.add_argument('--window-size=800,600')  # Set window size to 800x600
options.add_argument('--window-position=1600,100')

service = webdriver.ChromeService(executable_path=CHROME_WEBDRIVER)

options.add_argument(f"profile-directory=Profile 16")
# options.add_argument("--headless")
# options.add_argument("--log-level=3")
# options.add_argument('--window-size=1,1') 

driver = webdriver.Chrome(options=options, service=service)


driver.minimize_window()
driver.get("https://www.bing.com")
time.sleep(5)

for i in range(11):
        
    search = driver.find_element(by='name',value='q')
    search.clear()
    search.send_keys(list_item[i])
    time.sleep(1)
    search.send_keys(Keys.ENTER)
    time.sleep(6)

driver.quit()


options.add_argument(f"profile-directory=Profile 18")
driver = webdriver.Chrome(options=options, service=service)
# driver.set_window_position(-2000, 0) 
driver.minimize_window()
driver.get("https://www.bing.com")
time.sleep(5)
for i in range(11):
       
    search = driver.find_element(by='name',value='q')
    search.clear()
    search.send_keys(list_item[i])
    time.sleep(1)
    search.send_keys(Keys.ENTER)
    time.sleep(6)

driver.quit()


options.add_argument(f"profile-directory=Profile 17")
driver = webdriver.Chrome(options=options, service=service)
driver.minimize_window()
driver.get("https://www.bing.com")
time.sleep(5)
for i in range(11): 
        
    search = driver.find_element(by='name',value='q')
    search.clear()
    search.send_keys(list_item[i])
    time.sleep(1)
    search.send_keys(Keys.ENTER)
    time.sleep(6)

driver.quit()

options.add_argument(f"profile-directory=Profile 19")
driver = webdriver.Chrome(options=options, service=service)
driver.minimize_window()
driver.get("https://www.bing.com")
time.sleep(5)
for i in range(11):
    
    search = driver.find_element(by='name',value='q')
    search.clear()
    search.send_keys(list_item[i])
    time.sleep(1)
    search.send_keys(Keys.ENTER)
    time.sleep(6)

driver.quit()