import os
import glob
import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Determine if running in test mode
TEST_MODE = os.getenv('TEST_MODE', 'false').lower() == 'true'

# Set the ChromeDriver path from environment variables
chrome_driver_path = '/test/chromedriver' if TEST_MODE else os.getenv('CD_PATH')
if not chrome_driver_path:
    raise EnvironmentError("Missing ChromeDriver path (CD_PATH) in environment variables.")

def download_image_from_unsplash(search_term: str, download_path: str) -> str:
    """Download an image from Unsplash based on a search term and return its path."""
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--ignore-certificate-errors")

    try:
        with webdriver.Chrome(service=webdriver.chrome.service.Service(chrome_driver_path), options=options) as driver:
            driver.get('https://unsplash.com')
            search_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//input[@title="Search Unsplash"]')))
            search_box.send_keys(search_term + Keys.ENTER)

            download_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//a[@title="Download photo"]')))
            download_button.click()

            WebDriverWait(driver, 10).until(lambda d: len(glob.glob(f"{download_path}*.jpg")) > 0)

        image_path = max(glob.glob(f"{download_path}*"), key=os.path.getctime)
        logging.info(f"Image from Unsplash downloaded successfully to {image_path}.")
        return image_path
    except Exception as e:
        logging.error(f"Error downloading image from Unsplash: {e}")
        return None