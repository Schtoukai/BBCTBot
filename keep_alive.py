from flask import Flask
from threading import Thread
from waitress import serve

app = Flask('')

@app.route('/')
def home():
    return "BBCTBot is online !"

def run():
    serve(app, host="0.0.0.0", port=8080)

def keep_alive():
    thread = Thread(target=run)
    thread.start()