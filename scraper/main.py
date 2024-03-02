import time
from typing import Any
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import os
from scrapers.base_scraper import BaseScraper
from scrapers.job_boards.apple import AppleJobScraper
from scrapers.job_boards.amazon import AmazonJobScraper
from scrapers.job_boards.google import GoogleJobScraper
from scrapers.job_boards.microsoft import MicrosoftJobScraper
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/<target>")
def scrape_target(target):
    a = BaseScraper()
    match target:
        case 'apple':
            a = AppleJobScraper()
        case 'amazon':
            a = AmazonJobScraper()
        case 'google':
            a = GoogleJobScraper()
        case 'microsoft':
            a = MicrosoftJobScraper()
        case _:
            print(f'Error: target "{target}" does not match any valid target.')
    jobs = a.scrape()
    return json.dumps(jobs, indent=4)
