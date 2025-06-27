from flask import Flask, request
import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

@app.route('/notify', methods=['POST'])
def notify():
    data = request.json
    name = data.get("name")
    message = data.get("message")

    # Prepare email
    email_sender = os.getenv("EMAIL_SENDER")
    email_receiver = os.getenv("EMAIL_RECEIVER")
    smtp_username = os.getenv("SMTP_USERNAME")
    smtp_password = os.getenv("SMTP_PASSWORD")
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = int(os.getenv("SMTP_PORT", 587))

    body = f"""
    📬 New Feedback Received

    From: {name}
    Message:
    {message}
    """

    msg = MIMEText(body)
    msg["Subject"] = "🔔 Feedback Notification"
    msg["From"] = email_sender
    msg["To"] = email_receiver

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(email_sender, email_receiver, msg.as_string())
        server.quit()
        return {"status": "✅ Email sent"}, 200
    except Exception as e:
        print(f"❌ Email sending failed: {e}", flush=True)
        return {"status": "❌ Email failed"}, 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

