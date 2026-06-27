from flask import Flask
import socket
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "project":"Intelligent Load Balancing System",
        "server":socket.gethostname(),
        "status":"healthy",
        "timestamp":str(datetime.now())
    }

@app.route("/health")
def health():
    return {"status":"UP"}

@app.route("/version")
def version():
    return {"version":"1.0.0"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
