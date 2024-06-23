from selenium import webdriver
from selenium.webdriver.common.by import By
import json

from scrapers.base_scraper import BaseScraper

class RiotgamesJobScraper(BaseScraper):
    def scrape(self):
        browser = webdriver.Chrome()
        browser.implicitly_wait(20)

        jobs = []
        browser.get('https://www.riotgames.com/en/work-with-us/jobs#craft=software-engineering-group')

        elements = browser.find_element(By.CLASS_NAME, 'job-list__body').find_elements(By.CLASS_NAME, 'job-row')

        for e in elements:
            job_details = {}
            job_details['link'] = e.find_element(By.TAG_NAME, 'a').get_attribute('href')

            table_row_elements = e.find_elements(By.CLASS_NAME, 'job-row__col')
            
            job_details['title'] = table_row_elements[0].text
            job_details['group'] = table_row_elements[1].text
            job_details['team'] = table_row_elements[2].text
            job_details['location'] = table_row_elements[3].text

            jobs.append(job_details)

        return jobs

if __name__ == '__main__':
    a = RiotgamesJobScraper()
    a.scrape()