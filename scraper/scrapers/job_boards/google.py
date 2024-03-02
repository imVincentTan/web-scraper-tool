from selenium import webdriver
from selenium.webdriver.common.by import By
import json
from selenium.webdriver.chrome.options import Options

from scrapers.base_scraper import BaseScraper

class GoogleJobScraper(BaseScraper):  
    def scrape(self):
        options = Options()
        options.add_argument("--window-size=1920,1080")

        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(2)

        jobs = []

        browser.get('https://www.google.com/about/careers/applications/jobs/results/?category=DATA_CENTER_OPERATIONS&category=DEVELOPER_RELATIONS&category=HARDWARE_ENGINEERING&category=INFORMATION_TECHNOLOGY&category=MANUFACTURING_SUPPLY_CHAIN&category=NETWORK_ENGINEERING&category=PRODUCT_MANAGEMENT&category=PROGRAM_MANAGEMENT&category=SOFTWARE_ENGINEERING&category=TECHNICAL_INFRASTRUCTURE_ENGINEERING&category=TECHNICAL_SOLUTIONS&category=TECHNICAL_WRITING&q=')

        elements = browser.find_elements(By.CLASS_NAME, 'sMn82b')

        for e in elements:
            job_details = {}
            job_details['link'] = e.find_element(By.CLASS_NAME, 'VfPpkd-mRLv6').get_attribute('href')
            job_details['title'] = e.find_element(By.CLASS_NAME, 'QJPWVe').text
            job_details['location'] = e.find_element(By.CLASS_NAME, 'vo5qdf').find_element(By.CLASS_NAME, 'r0wTof').text

            jobs.append(job_details)

        return jobs
    
if __name__ == '__main__':
    a = GoogleJobScraper()
    a.scrape()