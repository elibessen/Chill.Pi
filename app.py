from flask import Flask, render_template, jsonify
import random
import time

app = Flask(__name__)

def get_temperature():
    return 32.5 

def get_fan_rpm():
    return 1450

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/status")
def status():
    data = {
        "temperature": get_temperature(),
        "rpm": get_fan_rpm(),
        "timestamp": time.time()
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)  