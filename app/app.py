from flask import Flask, jsonify
import logging

app = Flask(__name__)

# Configure logging to see requests in Docker logs
logging.basicConfig(level=logging.INFO)

@app.route('/')
def index():
    return "App is running!", 200

@app.route('/health')
def health():
    return jsonify(status="healthy"), 200

@app.route('/error')
def error():
    app.logger.error("Intentional 500 error triggered")
    return "Intentional Server Error", 500

if __name__ == '__main__':
    # Listen on all interfaces (required for Docker)
    app.run(host='0.0.0.0', port=5000)