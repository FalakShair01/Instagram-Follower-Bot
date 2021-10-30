import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

CHROME_DRIVER_PATH = "C:/Development/chromedriver.exe"
SIMILAR_ACCOUNT = "chefsteps"
EMAIL = "YOUR USERNAME/EMAIL"
PASSWORD = "YOUR PASSWORD"


class InstaFollower:
    def __init__(self, path):
        s = Service(path)
        self.driver = webdriver.Chrome(service=s)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)

        email = self.driver.find_element(By.NAME, "username")
        email.send_keys(EMAIL)

        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(PASSWORD)

        time.sleep(2)

        password.send_keys(Keys.ENTER)

        time.sleep(5)

        not_now_popup = self.driver.find_element(By.CSS_SELECTOR, ".cmbtv .sqdOP")
        not_now_popup.click()

        time.sleep(3)

        close_popup = self.driver.find_element(By.CSS_SELECTOR, ".mt3GC .HoLwm ")
        close_popup.click()

    def find_followers(self):
        time.sleep(3)

        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        time.sleep(3)

        followers = self.driver.find_element(By.PARTIAL_LINK_TEXT, 'followers')
        followers.click()
        time.sleep(3)

        followers_popup = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div[2]')

        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_popup)
            time.sleep(3)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for button in all_buttons:
            try:
                button.click()
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, "/html/body/div[7]/div/div/div/div[3]/button[2]")
                cancel_button.click()
            finally:
                time.sleep(2)


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()
