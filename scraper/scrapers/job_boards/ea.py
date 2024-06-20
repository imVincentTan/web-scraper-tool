from selenium import webdriver
from selenium.webdriver.common.by import By
import json

from scrapers.base_scraper import BaseScraper

class EaJobScraper(BaseScraper):
    def scrape(self):
        browser = webdriver.Chrome()
        browser.implicitly_wait(20)

        jobs = []
        browser.get('https://ea.gr8people.com/jobs?inp1810=4')

        elements = browser.find_element(By.CLASS_NAME, 'search-results-view').find_element(By.TAG_NAME, 'table').find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')

        for e in elements:
            job_details = {}
            job_details['link'] = e.find_element(By.TAG_NAME, 'a').get_attribute('href')
            job_details['company_id'] = e.find_element(By.TAG_NAME, 'a').text

            # table_row_elements = e.find_elements(By.TAG_NAME, 'td') # TODO: for some reason it can't find 'td' tag. find out if its selenium issue or what
            table_row_elements = e.find_elements(By.CLASS_NAME, 'search-results-column-left')
            
            job_details['title'] = table_row_elements[1].text
            job_details['location'] = table_row_elements[3].text
            job_details['remote'] = table_row_elements[4].text
            job_details['requisition_type'] = table_row_elements[5].text

            jobs.append(job_details)

        return jobs

if __name__ == '__main__':
    a = EaJobScraper()
    a.scrape()