from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import socket
from pymsgbox import confirm
import time
from text_create import list_item
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import smtplib
from selenium.common.exceptions import TimeoutException

my_email = "pankaj12016@outlook.com"
password = "amSparta@59"
message = """Subject: Desktop Rewards Alert


Desktop rewards are successfully collected.
"""
SLEEPTIME = 870
# STATUS = 0
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

def fetch_points(profile_path,options):
    global STATUS
    options.add_argument(profile_path)
    try:
        driver = webdriver.Chrome(options=options, service=service)
        driver.get("https://rewards.bing.com/pointsbreakdown")
        driver.implicitly_wait(5)

        points = driver.find_elements(By.CSS_SELECTOR,"p.pointsDetail.c-subheading-3.ng-binding")
        desktop = points[0].text.split()
        collected = int(desktop[0])
        total = int(desktop[2])
        STATUS = collected / total
        print(STATUS)
        print("Collected Rewards:")
        for i in points:
            print(i.text)
    except TimeoutException:
        driver.quit()
        fetch_points(profile_path,options)
    driver.quit()

def perfrom_task(profile_path,options):
    options.add_argument(profile_path)
    driver = webdriver.Chrome(options=options, service=service)
    driver.minimize_window()
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
            print("No tasks found")

    except NoSuchElementException:
        print("An error occurred while trying to find elements.")
    time.sleep(10)

    driver.quit()
    

CHROME_WEBDRIVER  = "chromedriver.exe"

options = webdriver.ChromeOptions()
profile = "C:/Users/Anil/AppData/Local/Google/Chrome/User Data/"

options.add_argument(f"user-data-dir=C:/Users/Anil/AppData/Local/Google/Chrome/User Data")  # Replace with your Chrome profile path
options.add_argument('--window-size=800,600')  # Set window size to 800x600
options.add_argument('--window-position=1600,100')
options.add_argument('--timeout=40')

service = webdriver.ChromeService(executable_path=CHROME_WEBDRIVER)

profiles = ["profile-directory=Profile 15"]
# level1 = ["profile-directory=Profile 19","profile-directory=Profile 17","profile-directory=Profile 18","profile-directory=Profile 16"]
wait_for_internet_connection()
# fetch_points(profiles[-1],options)
# if(STATUS == 0):
#     for profile in profiles:
#         perfrom_task(profile,options)
#     for profile in level1:
#         perfrom_task(profile,options)

# while STATUS != 1:
#     wait_for_internet_connection()
#     for profile in profiles:
#         perfrom_search(profile,options)
#     fetch_points(profiles[-1],options)
#     i+=1
#     if(i==11):
#         break
#     if(STATUS!=1):
#         time.sleep(SLEEPTIME)

for i in range(7):
    wait_for_internet_connection()
    for profile in profiles:
        perfrom_search(profile,options)
    # if(i<3):
    #     for profile in level1:
    #         perfrom_search(profile,options)
    # else:
    #     SLEEPTIME = 850
    if(i==6):
        break
    time.sleep(SLEEPTIME)



connection = smtplib.SMTP('smtp-mail.outlook.com',587)
connection.starttls()
connection.login(user=my_email,password=password)
connection.sendmail(from_addr=my_email,to_addrs="anil04jtn@gmail.com",msg=message)
connection.close()