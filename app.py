from flask import Flask, jsonify
import socket, os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Hello from Container!",
        "hostname": socket.gethostname(),
        "platform": os.environ.get("PLATFORM", "unknown")
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)