from flask import Flask
import subprocess
import os
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get full name
    name = "Your Full Name"  # Replace with your actual name

    # Get system username
    username = os.getenv("USER")

    # Get server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z')

    # Get htop output
    htop_output = subprocess.getoutput('top -b -n 1')

    # Display the result in HTML format
    return f"""
    <h1>HTop Output</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {server_time}</p>
    <pre>{htop_output}</pre>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
