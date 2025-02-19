import subprocess
from selenium import webdriver
import socket
from pymsgbox import confirm
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

DESKTOP_STATUS = 0
MOBILE_STATUS = 0

def fetch_points(profile_path,options):
    global DESKTOP_STATUS
    global MOBILE_STATUS

    options.add_argument(profile_path)
    try:
        driver = webdriver.Chrome(options=options, service=service)
        driver.get("https://rewards.bing.com/pointsbreakdown")
        driver.implicitly_wait(5)

        points = driver.find_elements(By.CSS_SELECTOR,"p.pointsDetail.c-subheading-3.ng-binding")
        desktop = points[0].text.split()
        mobile = points[1].text.split()
        desktop_collected = int(desktop[0])
        desktop_total = int(desktop[2])
        mobile_collected = int(mobile[0])
        mobile_total = int(mobile[2])
        DESKTOP_STATUS = desktop_collected / desktop_total
        MOBILE_STATUS = mobile_collected / mobile_total
        print(DESKTOP_STATUS)
        print(MOBILE_STATUS)
        print("Collected Rewards:")
        for i in points:
            print(i.text)
    except TimeoutException:
        driver.quit()
        fetch_points(profile_path,options)
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


CHROME_WEBDRIVER  = "chromedriver.exe"

options = webdriver.ChromeOptions()
profile = "C:/Users/Anil/AppData/Local/Google/Chrome/User Data/"

options.add_argument(f"user-data-dir=C:/Users/Anil/AppData/Local/Google/Chrome/User Data")  # Replace with your Chrome profile path
options.add_argument('--window-size=800,600')  # Set window size to 800x600
# options.add_argument('--window-position=1600,100')
options.add_argument('--timeout=40')

service = webdriver.ChromeService(executable_path=CHROME_WEBDRIVER)

profile = "profile-directory=Profile 12"
fetch_points(profile,options)

if(MOBILE_STATUS!=1):
    subprocess.run(["python", "chrome mobile.py"])
else:
    print("Mobile Rewards are already collected.")
if(DESKTOP_STATUS!=1):
    subprocess.run(["python", "desktop.py"])
else:
    print("Desktop rewards are already collected.")