from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "BBCTBot is online !"

def run():
    if __name__ == "__main__":
        from waitress import serve
        serve(app, host="0.0.0.0", port=8080)
    else:
        app.run(host="0.0.0.0", port=8080)

def keep_alive():
    thread = Thread(target=run)
    thread.start()