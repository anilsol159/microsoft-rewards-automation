from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
import time

# Set the path to your Vivaldi user data directory
user_data_dir = "C:/Users/Anil/AppData/Local/Vivaldi/User Data/Profile 1"  # Replace with your actual path

# Create a ChromeOptions object to specify the profile
CHROME_WEBDRIVER  = "chromedriver.exe"

options = webdriver.ChromeOptions()
options.binary_location= 'C:/Users/Anil/AppData/Local/Vivaldi/Application/vivaldi.exe'
options.add_argument("user-data-dir={}".format(user_data_dir))

# Create a WebDriver instance for Vivaldi
service = webdriver.ChromeService(executable_path=CHROME_WEBDRIVER)
driver = webdriver.Chrome(options=options, service=service)
driver.get("https://www.bing.com")
time.sleep(15)
# Interact with the website as needed
# (e.g., find elements, click buttons, fill forms)

# Close the browser when finished
driver.quit()