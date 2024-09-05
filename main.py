from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from dotenv import load_dotenv

load_dotenv()

twitter_email = os.environ["TWITTER_EMAIL"]
twitter_password = os.environ["TWITTER_PASSWORD"]
phone_or_username = os.environ["TWITTER_USERNAME"]
url = "https://x.com/i/flow/login"
key_word = "#m4_bvg"
XPATH_SEARCH_BOX = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/div/div[2]/div/input'

# Keep Chrome browser open after the program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

time.sleep(7)  # Give time for the login page to load

username_input = driver.find_element(By.NAME, "text")
username_input.send_keys(twitter_email, Keys.ENTER)

time.sleep(5)

phone_or_username_input = driver.find_element(By.XPATH, '//input[@name="text"]')
phone_or_username_input.send_keys(phone_or_username, Keys.ENTER)

time.sleep(7)


password_input = driver.find_element(By.NAME, "password")
password_input.send_keys(twitter_password, Keys.ENTER)

time.sleep(5)

search_box = driver.find_element(By.XPATH, XPATH_SEARCH_BOX)
search_box.send_keys(key_word, Keys.ENTER)

time.sleep(3)

# Navigate to "Latest" tweets tab
latest_tab_xpath = '//a[@href="/search?q=%23m4_bvg&src=typed_query&f=live"]'
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, latest_tab_xpath)))
latest_tab = driver.find_element(By.XPATH, latest_tab_xpath)
latest_tab.click()

time.sleep(5)

# Fetch the latest tweet text
latest_tweet_xpath = '//article[@role="article"][1]//div[@dir="auto"]/span'
latest_tweet = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, latest_tweet_xpath))
)
print(latest_tweet.text)
