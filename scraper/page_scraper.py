from selenium import webdriver
from selenium.webdriver.common.by import By
import json

if __name__ == '__main__':
    browser = webdriver.Chrome()
    url = ''
    browser.get(url)

    elements = browser.find_elements(By.CLASS_NAME, "job-link")

    jobs = []

    for e in elements:
        job_details = {}
        job_details['link'] = e.get_attribute('href')
        job_details['posting-date'] = e.find_element(By.CLASS_NAME, 'posting-date').text
        job_details['last-updated'] = e.find_element(By.CLASS_NAME, 'time-elapsed').text
        jobs.append(job_details)

    print(json.dumps(jobs, indent=4))
