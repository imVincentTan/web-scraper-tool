from typing import Any
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import os

data: list[dict[str, Any]]
with open(os.path.abspath('data.json'), 'r') as json_file:
    data = json.load(json_file)

def get_by_from_attribute(attribute: str):
    retval: Any
    match attribute:
        case 'class':
            retval = By.CLASS_NAME
    return retval
    
def eval_command(element, command: list[str]):
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

def parse_selection(element, commands: list[list[str]]):
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