from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from text_create import list_item

EDGE_WEBDRIVER  = "msedgedriver.exe"
service = webdriver.EdgeService(executable_path=EDGE_WEBDRIVER)
driver = webdriver.Edge(service=service)
driver.get("https://www.bing.com")
time.sleep(15)


for item in list_item:
    search = driver.find_element(by='name',value='q')
    search.clear()
    search.send_keys(item)
    time.sleep(1)
    search.send_keys(Keys.ENTER)
    time.sleep(10)

# chatting
# chat = driver.find_element(by='id',value='b-scopeListItem-conv')
# chat.click()
# time.sleep(20)
    







