import time
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/data")
def ret_data():
    pets = {"cats": {"num": 3, "names": ["fluffy", "snowball", "garfield"]}, "dogs": None}
    return pets

@app.route("/sleep/<amt>")
def slp(amt):
    time.sleep(int(amt))
    return f"Slept for {amt} seconds"

@app.route("/login/<name>")
def login(name):
    return f"Congrats on logging in {name}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224, debug=True)
