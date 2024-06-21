import json
from flask import Flask
import requests
import psycopg2
from psycopg2 import extras

from cleaners.base_cleaner import BaseCleaner
from cleaners.job_boards.amazon import AmazonJobCleaner
from cleaners.job_boards.apple import AppleJobCleaner
from cleaners.job_boards.ea import EaJobCleaner
from cleaners.job_boards.google import GoogleJobCleaner
from cleaners.job_boards.microsoft import MicrosoftJobCleaner

app = Flask(__name__)

# TODO: put this stuff into some config file
SCRAPER = 'http://127.0.0.1:5000'
conn = psycopg2.connect(
    host = 'localhost',
    dbname = 'postgres',
    user = 'postgres',
    password = 'password',
    port = 5432
)
# TODO: put the connections and cursors in the right place
cur = conn.cursor()

target_string_to_cleaner = {
    'apple': AppleJobCleaner,
    'amazon': AmazonJobCleaner,
    'ea': EaJobCleaner,
    'google': GoogleJobCleaner,
    'microsoft': MicrosoftJobCleaner
}

@app.route("/")
def hello_world():
    return "Hello, World! i clean and load into some db"

@app.route("/job_boards/<target>")
def load_target(target):
    retval = None
    if target == 'all':
        retval = {}
        for key in target_string_to_cleaner:
            retval[key] = json.loads(load_target_helper(key))
        retval = json.dumps(retval, indent=4)
    else:
        retval = load_target_helper(target)
    return retval

def load_target_helper(target):
    cleaner = BaseCleaner(None)
    r = requests.get(f"{SCRAPER}/{target}")

    if target in target_string_to_cleaner:
        cleaner = target_string_to_cleaner[target](r.json())
    else:
        print(f'Error: target "{target}" does not match any valid target.')

    clean_input = cleaner.get_clean_data()
    columns = ['company', 'company_id', 'link', 'title', 'location', 'posting_date', 'last_updated', 'details']

    query = f"""INSERT INTO public.jobs ({", ".join(columns)}) VALUES %s ON CONFLICT DO NOTHING"""
    
    extras.execute_values(cur, query, clean_input)

    conn.commit()
    
    return r.content

if __name__ == "__main__":
    print('starting loader app on port 5001:')
    app.run(host='127.0.0.1', port='5001')
