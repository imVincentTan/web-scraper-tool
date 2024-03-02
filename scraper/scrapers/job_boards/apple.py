from selenium import webdriver
from selenium.webdriver.common.by import By
import json

from scrapers.base_scraper import BaseScraper

class AppleJobScraper(BaseScraper):   
    def scrape(self):
        
        browser = webdriver.Chrome()
        browser.implicitly_wait(2)

        jobs = []

        browser.get('https://jobs.apple.com/en-us/search?team=natural-language-processing-and-speech-technologies-MLAI-NLP+computer-vision-MLAI-CV+applied-research-MLAI-AR+apps-and-frameworks-SFTWR-AF+cloud-and-infrastructure-SFTWR-CLD+core-operating-systems-SFTWR-COS+devops-and-site-reliability-SFTWR-DSR+engineering-project-management-SFTWR-EPM+information-systems-and-technology-SFTWR-ISTECH+machine-learning-and-ai-SFTWR-MCHLN+security-and-privacy-SFTWR-SEC+software-quality-automation-and-tools-SFTWR-SQAT+wireless-software-SFTWR-WSFT+machine-learning-infrastructure-MLAI-MLI+deep-learning-and-reinforcement-learning-MLAI-DLRL')

        elements = browser.find_element(By.CLASS_NAME, 'results__table').find_elements(By.TAG_NAME, 'tbody')

        for e in elements:
            job_details = {}
            job_details['link'] = e.find_element(By.CLASS_NAME, 'table-col-1').find_element(By.TAG_NAME, 'a').get_attribute('href')
            job_details['posting_date'] = e.find_element(By.CLASS_NAME, 'table--advanced-search__date').text

            job_details['title'] = e.find_element(By.CLASS_NAME, 'table-col-1').find_element(By.TAG_NAME, 'a').text
            job_details['location'] = e.find_element(By.CLASS_NAME, 'table-col-2').find_element(By.TAG_NAME, 'span').text
            job_details['team'] = e.find_element(By.CLASS_NAME, 'table--advanced-search__role').text

            jobs.append(job_details)

        return jobs
    
if __name__ == '__main__':
    a = AppleJobScraper()
    a.scrape()