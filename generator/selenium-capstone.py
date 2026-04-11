from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time
import random

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1280,720")

for attempt in range(10):
    try:
        driver = webdriver.Remote(
            command_executor="http://chrome-browser:4444/wd/hub",
            options=options
        )
        print("Connected to Selenium")
        break
    except Exception as e:
        print(f"[!] Attempt {attempt + 1} failed: {e}")
        time.sleep(5)

if driver is None:
    raise RuntimeError("[X] Could not connect to Selenium after multiple attempts")

for attempt in range(15):
    try:
        driver.get("http://umami:3000/script.js")
        print("[!] Umami is reachable")
        break
    except Exception as e:
        print(f"Umami attempt {attempt + 1} failed: {e}")
        time.sleep(3)
else:
    raise RuntimeError("[X] Umami never became reachable")


class TrafficGenerator:
    def __init__(self, urls):
        self.urls = urls

    def generateRandomTime(self):
        return random.randint(1, 5)
    
    def getUrls(self):
        for url in self.urls:
            print(f"[!] Getting URL: {url} now...")
            driver.get(url)

            time.sleep(self.generateRandomTime())



if __name__ == "__main__":

    urls = ["http://otterwiki/", "http://otterwiki/-/create"]
    generator = TrafficGenerator(urls)
    generator.getUrls()
    print(f"[!] Finished running script.")
