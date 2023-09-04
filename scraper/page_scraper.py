from typing import Any
from selenium import webdriver
from selenium.webdriver.common.by import By
import json

data = [
    {
        'id': '',
        'url': '',
        'listing_element': [['find_elements', 'class', 'job-link']],
        'targets': {
            'link': [['get_attribute', 'href']],
            'posting_date': [['find_element', 'class', 'posting-date'], ['text']],
            'last_updated': [['find_element', 'class', 'time-elapsed'], ['text']]
        }
    }
]

def get_by_from_attribute(attribute):
    retval: Any
    match attribute:
        case 'class':
            retval = By.CLASS_NAME
    return retval
    
def eval_command(element, command):
    retval: Any
    match command[0]:
        case 'find_elements':
            retval = element.find_elements(get_by_from_attribute(command[1]), command[2])
        case 'find_element':
            retval = element.find_element(get_by_from_attribute(command[1]), command[2])
        case 'get_attribute':
            retval = element.get_attribute(command[1])
        case 'text':
            retval = element.text
    return retval

def parse_selection(element, commands):
    retval = element
    for command in commands:
        retval = eval_command(retval, command)
    return retval

if __name__ == '__main__':
    browser = webdriver.Chrome()
    jobs = []

    for d in data:    
        browser.get(d['url'])
        elements = parse_selection(browser, d['listing_element'])
        for e in elements:
            job_details = {'id': d['id']}
            job_details['targets'] = {}
            for t in d['targets']:
                job_details['targets'][t] = parse_selection(e, d['targets'][t])
            jobs.append(job_details)

    print(json.dumps(jobs, indent=4))