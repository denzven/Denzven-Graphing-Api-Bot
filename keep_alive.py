from flask import Flask
from threading import Thread

app = Flask('')
@app.route('/')

def home():
    return"DenzGraphingApiWrapper_Bot is up and running"
    
def run():
    app.run(port='8080', host='0.0.0.0')

def keep_alive():
   t = Thread(target = run)
   t.start()