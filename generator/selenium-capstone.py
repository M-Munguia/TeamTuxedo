from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import os
import time
import random
import requests

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
    
    def login(self):
        r = requests.post(
        "http://umami:3000/api/auth/login",
        json={"username": "admin", "password": "umami"},
        )
        r.raise_for_status()
        return r.json()["token"]
    
    def checkWebsiteExists(self, token):
        #checks if a website already exists, if it does, it skips the other steps
        if os.path.exists("/shared/custom-files/umami_website_id.txt"):
            with open("/shared/custom-files/umami_website_id.txt") as reader:
                id = reader.read().strip()
                print("ID is: " + str(id))
                if not id:
                    return False
        else:
            return False
        
        response = requests.get(f"http://umami:3000/api/websites/{id}", headers = {"Authorization": f"Bearer {token}"})
        if response.status_code == 200:
            return True
        
        return False
    
    def createWebsite(self, token):
        #creates a website and returns the ID to inject into the script and html files
        response = requests.post("http://umami:3000/api/websites", headers = {"Authorization": f"Bearer: {token}"}, json = {"name":"Otterwiki","domain":"localhost:8080"})
        if "id" in response.text:
            print(f"[!] Created website: {response.json()['id']}")
            return response.json()['id']

        print(f"[!] Failed to create website.")
        exit(1)
    
    def writeWebsiteID(self, token, id):
        #takes the returned website ID and puts it into the files.
        js = f'<script defer src="http://umami:3000/script.js" data-website-id="{id}"></script>'
        html = f'<script defer src="http://umami:3000/script.js" data-website-id="{id}"></script>'
        with open("/shared/custom-files/customHead.html", "w") as f:
            f.write(js)
        with open("/shared/custom-files/customHead.js", "w") as f:
            f.write(js)

        with open("/shared/custom-files/umami_website_id.txt", "w") as f:
            f.write(id)

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

    token = generator.login()
    if not generator.checkWebsiteExists(token):
        print('[!] Website not created... Creating it now.')
        websiteId = generator.createWebsite(token)
        generator.writeWebsiteID(token, websiteId)

    generator.getUrls()
    print(f"[!] Finished running script.")
