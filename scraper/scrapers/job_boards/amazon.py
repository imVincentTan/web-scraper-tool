from selenium import webdriver
from selenium.webdriver.common.by import By
import json

from scrapers.base_scraper import BaseScraper

class AmazonJobScraper(BaseScraper):
    def scrape(self):
        browser = webdriver.Chrome()
        browser_helper = webdriver.Chrome()
        browser.implicitly_wait(2)
        browser_helper.implicitly_wait(2)

        jobs = []

        browser.get('https://www.amazon.jobs/en/job_categories/software-development?sort=recent')

        elements = browser.find_element(By.XPATH, "//*[contains(@class,'jobs-module')]").find_elements(By.TAG_NAME, 'li')

        for e in elements:
            job_details = {}
            job_details['link'] = e.find_element(By.TAG_NAME, 'a').get_attribute('href')
            job_details['last_updated'] = e.find_element(By.XPATH, "//*[contains(text(),'Updated:')]").text

            browser_helper.get(job_details['link'])
            job_details['title'] = browser_helper.find_element(By.TAG_NAME, 'h1').text
            job_details['location'] = browser_helper.find_element(By.CLASS_NAME, 'location-icon').text

            jobs.append(job_details)

        return jobs

if __name__ == '__main__':
    a = AmazonJobScraper()
    a.scrape()