from flask import Flask, request
import sqlite3
import os
import requests

app = Flask(__name__)
DB_PATH = "/data/feedback.db"

# Create database if it doesn't exist
def init_db():
    os.makedirs("/data", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            message TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return '''
        <h2>Feedback Form</h2>
        <form action="/submit" method="post">
            Name: <input name="name"><br><br>
            Message:<br>
            <textarea name="message"></textarea><br><br>
            <input type="submit" value="Submit">
        </form>
    '''

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    message = request.form['message']

    # Save to SQLite DB
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO feedback (name, message) VALUES (?, ?)", (name, message))
    conn.commit()
    conn.close()

    # Notify the second microservice
    try:
        response = requests.post("http://notifier:5000/notify", json={
            "name": name,
            "message": message
        })
        print(f"Notifier response: {response.status_code}")
    except Exception as e:
        print(f"Notifier service failed: {e}")

    return f"<h3>Thank you, {name}! Your feedback was saved and notification sent.</h3>"

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=80)
