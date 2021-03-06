# pip3 install selenium
# pip3 install bs4
# pip3 install python-dotenv
# in virtualenv ScrapeYardTest

# need to download WebDriver binary and add to PATH -- chromedriver 86
# put the chromedriver binary in this directory for now and it works so w/e

# template copied from https://github.com/mross1080/WebScrapingWorkshop/blob/master/scrape_ig.py

from dotenv import load_dotenv
load_dotenv()

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import os

from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# taggee_class = "_hli"

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")

driver = webdriver.Chrome(executable_path=DRIVER_BIN)

# print(__file__);

# Begin Template Code

driver.get('https://www.instagram.com/accounts/login/?hl=en')

print("Opened instagram")

sleep(1)

username_box = driver.find_element_by_name('username')
username_box.send_keys(os.getenv("ACCOUNT"))
print("Email Id entered")

password_box = driver.find_element_by_name('password')
password_box.send_keys(os.getenv("PASSWORD"))
print("Password entered")
#

login_box = driver.find_elements(By.XPATH, '//button')[1]
login_box.click()
#
sleep(1)

# now go to page

hashtag_url = "https://www.instagram.com/jameshosken/"

print("Opening {}".format(hashtag_url))
sleep(4)
driver.get(hashtag_url)
sleep(1)
print("Browsing Photos")
sleep(.5)

#  what's the "w" for?
outF = open("./testTxts/james.txt", "w") 

# stillScraping = true
# while stillScraping:
#     try:
#         soup_a = BeautifulSoup(driver.page_source, "html.parser")
#         for link in soup_a.find_all('img'):
#             # link.get('href') gets the href/url out of the a element
#             print(link.get('src'))
#             outF.write(link.get('src'))
#             outF.write("\n")
#         last_src_current_page = page_elements[-1].get_property("src")
#         print(last_src_current_page)
#     except Exception as e:
#         print(e)

while True:
    page_elements = driver.find_elements(By.XPATH, '//img')
    print("{} many elements on the page ".format(len(page_elements)))

    # Scroll to next area of page and load in new images
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    sleep(1)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    print(new_height)


    try:
        soup_a = BeautifulSoup(driver.page_source, "html.parser")
        for link in soup_a.find_all('img'):
            # link.get('href') gets the href/url out of the a element
            print(link.get('src'))
            outF.write(link.get('src'))
            outF.write("\n")
        last_src_current_page = page_elements[-1].get_property("src")
        print(last_src_current_page)


    except Exception as e:
        print(e)


sleep(1)
print("starting iteration ")