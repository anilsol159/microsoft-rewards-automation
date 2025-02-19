from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import socket
from pymsgbox import confirm
import time
from text_create import list_item
from selenium.webdriver.common.by import By
import smtplib
from selenium.common.exceptions import TimeoutException

my_email = "pankaj12016@outlook.com"
password = "amSparta@59"
message = """Subject: Mobile Rewards Alert


Mobile rewards are successfully collected.
"""

STATUS = 0
i = 0

def perfrom_search(profile_path,options):
    options.add_argument(profile_path)

    try:
        driver = webdriver.Chrome(options=options, service=service)
        driver.minimize_window()
        driver.get("https://www.bing.com")
        time.sleep(7)
        for j in range(4):
            
            
            search = driver.find_element(by='name',value='q')
            search.clear()
            search.send_keys(list_item[4*i+j])
            time.sleep(1)
            search.send_keys(Keys.ENTER)
            time.sleep(6)
    except TimeoutException:
        driver.quit()
        perfrom_search(profile_path,options)

    driver.quit()
def is_internet_connected():
    try:
        # Try to connect to a well-known website (Google DNS)
        socket.create_connection(("8.8.8.8", 53), timeout=5)
        return True
    except OSError:
        return False

def wait_for_internet_connection():
    while not is_internet_connected():
        # Display a pop-up message
        response = confirm(
            text="No internet connection detected. Do you want to retry?",
            title="Internet Connection",
            buttons=["Yes", "No"]
        )

        if response == "Yes":
            continue
        else:
            exit()

# def fetch_points(profile_path,options):
#     global STATUS
#     options.add_argument(profile_path)
#     try:
#         driver = webdriver.Chrome(options=options, service=service)
#         driver.get("https://rewards.bing.com/pointsbreakdown")
#         driver.implicitly_wait(5)

#         points = driver.find_elements(By.CSS_SELECTOR,"p.pointsDetail.c-subheading-3.ng-binding")
#         mobile = points[1].text.split()
#         collected = int(mobile[0])
#         total = int(mobile[2])
#         STATUS = collected / total
#         print(STATUS)
#         print("Collected Rewards:")
#         for i in points:
#             print(i.text)
#     except TimeoutException:
#         driver.quit()
#         fetch_points(profile_path,options)
#     driver.quit()


CHROME_WEBDRIVER  = "chromedriver.exe"

options = Options()
profile = "C:/Users/Anil/AppData/Local/Google/Chrome/User Data/"
options.add_argument('--window-size=800,600')  # Set window size to 800x600
options.add_argument('--window-position=1600,100')
options.add_argument('--timeout=40')


options.add_argument(f"user-data-dir=C:/Users/Anil/AppData/Local/Google/Chrome/User Data")  # Replace with your Chrome profile path
options.add_experimental_option("mobileEmulation", {"deviceName": "iPhone X"}) 

service = webdriver.ChromeService(executable_path=CHROME_WEBDRIVER)

profiles = ["profile-directory=Profile 15"]

# fetch_points(profiles[-1],options)

for i in range(5):
    wait_for_internet_connection()
    for profile in profiles:
        perfrom_search(profile,options)
    # if(i<3):
    #     for profile in level1:
    #         perfrom_search(profile,options)
    # else:
    #     SLEEPTIME = 850
    if(i==4):
        break
    time.sleep(880)

connection = smtplib.SMTP('smtp-mail.outlook.com',587)
connection.starttls()
connection.login(user=my_email,password=password)
connection.sendmail(from_addr=my_email,to_addrs="anil04jtn@gmail.com",msg=message)
connection.sendmail(from_addr=my_email,to_addrs="lokesh13122003@gmail.com",msg=message)
connection.close()
