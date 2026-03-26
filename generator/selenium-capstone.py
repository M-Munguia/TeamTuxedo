from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time
import random

options = Options()
driver = webdriver.Remote(
    command_executor="http://chrome-browser:4444/wd/hub",
    options=options
)


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

    urls = ["https://google.com", "https://youtube.com"]
    generator = TrafficGenerator(urls)
    generator.getUrls()
    print(f"[!] Finished running script.")
