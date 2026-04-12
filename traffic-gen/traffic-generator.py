from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import random

BASE_URL = "http://otterwiki"

PAGES = [
    "/",
    "/Home",
    "/-/index",
    "/-/create",
    "/-/help",
    "/-/search",
    "/Home/history",
]

def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")

    driver = webdriver.Remote(
        command_executor="http://selenium:4444/wd/hub",
        options=options
    )
    return driver

def random_delay():
    return random.uniform(2, 5)

def generate_traffic(iterations):
    time.sleep(60)
    driver = setup_driver()

    try:
        for i in range(iterations):
            page = random.choice(PAGES)
            url = BASE_URL + page

            print(f"Visit {i+1} to {url}")
            driver.get(url)

            time.sleep(random_delay())
    finally:
        driver.quit()

def main():
    generate_traffic(10)

if __name__ == "__main__":
    main()