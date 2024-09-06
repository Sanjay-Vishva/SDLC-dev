from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import pytz
from datetime import datetime

app = Flask(__name__, static_folder='static')
CORS(app)  # Enable CORS for all routes

# Cache for storing time data
cache = {}
cache_timeout = 60  # Cache timeout in seconds
last_fetch_time = 0

# Function to get the current time for a given city
def get_time(timezone):
    tz = pytz.timezone(timezone)
    current_time = datetime.now(tz)
    formatted_time = current_time.strftime('%d-%m-%Y - %H:%M:%S')
    return formatted_time

@app.route('/time')
def time():
    cities = {
        "New York": "America/New_York",
        "London": "Europe/London",
        "Tokyo": "Asia/Tokyo",
        "Sydney": "Australia/Sydney",
        "Berlin": "Europe/Berlin",
        "Mumbai": "Asia/Kolkata"
    }

    times = {city: get_time(timezone) for city, timezone in cities.items()}
    return jsonify(times)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True)
