from flask import Flask, jsonify, render_template, request
import logging

app = Flask(__name__)

# Configuring logging to see requests in Docker logs
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # This is where the backend "grabs" the data from the form
        user = request.form.get('username')
        pw = request.form.get('password')

        # Simple logic (In a real app, check a database here!)
        if user == "sandip" and pw == "password123":
            print(f"LOG: User {user} logged in successfully!")
            return f"Welcome, {user}!", 200
        else:
            print("LOG: Failed login attempt.")
            return "Invalid Credentials", 401

    # If the method is GET, just show the login page
    return render_template('login.html')

if __name__ == '__main__':
    # Listen on all interfaces (required for Docker)
    app.run(host='0.0.0.0', port=5000)