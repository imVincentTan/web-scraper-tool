from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import json

from scrapers.base_scraper import BaseScraper

class MicrosoftJobScraper(BaseScraper):  
    def scrape(self):
        options = Options()
        options.add_argument("--window-size=1920,1080")

        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(5)

        jobs = []

        browser.get('https://jobs.careers.microsoft.com/global/en/search?p=Software%20Engineering&l=en_us&pg=1&pgSz=20&o=Recent')

        elements = browser.find_element(By.CLASS_NAME, 'ms-List').find_elements(By.CLASS_NAME, 'ms-List-cell')

        for i in range(len(browser.find_element(By.CLASS_NAME, 'ms-List').find_elements(By.CLASS_NAME, 'ms-List-cell'))):
            browser.find_element(By.CLASS_NAME, 'ms-List').find_elements(By.CLASS_NAME, 'ms-List-cell')[i].click()
            job_details = {}
            job_details['link'] = browser.current_url

            job_description = browser.find_element(By.CLASS_NAME, 'SearchJobDetailsCard')

            job_details['title'] = job_description.find_element(By.TAG_NAME, 'h1').text
            job_details['location'] = job_description.find_element(By.XPATH, "//h1/following-sibling::div").text
            job_details['posting_date'] = job_description.find_element(By.XPATH, "//*[contains(text(),'Date posted')]/following-sibling::div").text

            jobs.append(job_details)

        return jobs
    
if __name__ == '__main__':
    a = MicrosoftJobScraper()
    a.scrape()