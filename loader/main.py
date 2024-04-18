from flask import Flask
import requests

app = Flask(__name__)
SCRAPER = 'http://127.0.0.1:5000'

@app.route("/")
def hello_world():
    return "Hello, World! i clean and load into some db"

@app.route("/<target>")
def load_target(target):
    r = requests.get(f"{SCRAPER}/{target}")
    return r.content

if __name__ == "__main__":
    print('starting loader app on port 5001:')
    app.run(host='127.0.0.1', port='5001')
