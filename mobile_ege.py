from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys
import time
from text_create import list_item

# Set Edge options for mobile view
EDGE_WEBDRIVER  = "msedgedriver.exe"
service = webdriver.EdgeService(executable_path=EDGE_WEBDRIVER)
options = Options()
options.use_chromium = True  # Ensure Chromium-based Edge is used
options.add_experimental_option("mobileEmulation", {"deviceName": "iPhone X"})  # Set specific mobile device

# Create a WebDriver instance
driver = webdriver.Edge(options=options,service=service)

# Navigate to the desired website
website_url = "https://www.bing.com"  # Replace with the actual website
driver.get(website_url)
time.sleep(10)

for i in range(21):
    search = driver.find_element(by='name',value='q')
    search.clear()
    search.send_keys(list_item[i])
    time.sleep(1)
    search.send_keys(Keys.ENTER)
    time.sleep(235)

# Close the browser when finished
driver.quit()