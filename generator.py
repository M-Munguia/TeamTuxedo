from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import random

# Configuration
SELENIUM_URL = "http://chrome-browser:4444/wd/hub"
TARGET_URLS = ["http://otterwiki/", "http://otterwiki/-/create", "http://otterwiki/Home"]
UMAMI_CHECK = "http://umami:3000/script.js"

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")


def connect_to_selenium(retries=10):
    for i in range(retries):
        try:
            driver = webdriver.Remote(command_executor=SELENIUM_URL, options=options)
            print("Connected to Selenium grid.")
            return driver
        except Exception as e:
            print(f"Connection attempt {i+1} failed: {e}")
            time.sleep(5)
    raise RuntimeError("Failed to connect to Selenium grid")

def wait_for_service(driver, url, retries=15):
    for i in range(retries):
        try:
            driver.get(url)
            print(f"Service at {url} is reachable.")
            return True
        except Exception:
            print(f"Waiting for service {url}... ({i+1})")
            time.sleep(3)
    return False

class TrafficGenerator:
    def __init__(self, driver, urls):
        self.driver = driver
        self.urls = urls

    def run(self, cycles=5):
        for i in range(cycles):
            print(f"Starting cycles {i+1}")
            random.shuffle(self.urls)
            for url in self.urls:
                print(f"Visiting: {url}")
                self.driver.get(url)
                time.sleep(random.uniform(2, 8))
    
    def randomURLTime(self):
        return random.randint(1, 9)
    

    def get(self):
        for url in self.urls:
            print(f"[!] getting urls: {url}")
            
            self.driver.get(url)

            time.sleep(self.randomURLTime())

if __name__ == "__main__":
    driver = connect_to_selenium()
    
    if wait_for_service(driver, UMAMI_CHECK):
        generator = TrafficGenerator(driver, TARGET_URLS)
        generator.run(cycles=3)
        generator.get()
        print("Traffic generation is complete.")
    
    driver.quit()




