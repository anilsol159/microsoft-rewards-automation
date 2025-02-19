from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from text_create import list_item
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


CHROME_WEBDRIVER  = "chromedriver.exe"

options = webdriver.ChromeOptions()
profile = "C:/Users/Anil/AppData/Local/Google/Chrome/User Data/"

options.add_argument(f"user-data-dir=C:/Users/Anil/AppData/Local/Google/Chrome/User Data")  # Replace with your Chrome profile path


service = webdriver.ChromeService(executable_path=CHROME_WEBDRIVER)

options.add_argument(f"profile-directory=Profile 10")

driver = webdriver.Chrome(options=options, service=service)


driver.get("https://rewards.bing.com/pointsbreakdown")
time.sleep(4)

points = driver.find_elements(By.CSS_SELECTOR,"p.pointsDetail.c-subheading-3.ng-binding")
print("Collected Rewards:")
for i in points:
    print(i.text)

driver.get("https://rewards.bing.com")
time.sleep(4)
try:
    # Find all elements with the text symbol '+'
    plus_elements = driver.find_elements(By.CSS_SELECTOR,"span.mee-icon.mee-icon-AddMedium")

    # Check if there are any '+' symbols
    if plus_elements:
        # Iterate through the elements and click each one
        for plus_element in plus_elements:
            plus_element.click()
            # Handle any additional actions after clicking if needed
    else:
        print("No '+' symbols found on the page.")

except NoSuchElementException:
    print("An error occurred while trying to find elements.")
time.sleep(10)

driver.quit()