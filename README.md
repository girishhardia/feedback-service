# 📨 Feedback Microservice App (Dockerized with Email Alerts)

This project is a **Docker-based microservice feedback system** that allows users to submit feedback through a web interface. It stores the feedback locally and sends email notifications using AWS SES.

> ✅ Built with: Flask, Nginx, Docker Compose, EC2, SES

---

## 🔧 Tech Stack

| Component   | Tech Used         | Description                            |
|-------------|-------------------|----------------------------------------|
| Frontend    | HTML + Nginx      | Static feedback form UI                |
| Notifier    | Flask + SMTP      | Sends feedback via email using SES     |
| Feedback DB | Python + SQLite   | Logs feedback messages locally         |
| Orchestration | Docker Compose | Connects and runs all services         |
| Cloud       | AWS EC2 + SES     | Hosted backend and SMTP mailer         |

---

## 🌐 Features

- 📝 Submit feedback via browser
- 📬 Sends emails via AWS SES
- 🗃️ Logs feedback data into a volume
- 🚀 Deployed on Amazon Linux EC2
- 🐳 Fully Dockerized: `docker-compose` ready

---

## 📁 Project Structure

```bash
feedback-service/
├── docker-compose.yml
├── frontend/
│   └── index.html
├── notifier/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .env         # contains SMTP credentials
├── feedback/
│   ├── app.py
│   └── Dockerfile
```
---

🚀 How to Run
1. 🐳 Install Docker (if not already):
bash
Copy
Edit
sudo yum install docker -y
sudo service docker start
2. 📦 Install Docker Compose Plugin
If docker compose isn't available:

bash
Copy
Edit
sudo curl -L https://github.com/docker/compose/releases/download/v2.24.6/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
3. 🛠️ Clone the Project
bash
Copy
Edit
git clone https://github.com/your-username/feedback-service.git
cd feedback-service
4. ⚙️ Add Environment Variables
In notifier/.env:

env
Copy
Edit
SMTP_USERNAME=your-smtp-username
SMTP_PASSWORD=your-smtp-password
SMTP_SERVER=email-smtp.us-east-1.amazonaws.com
SMTP_PORT=587
TO_EMAIL=you@example.com
FROM_EMAIL=verified@yourdomain.com
🔐 If SES is in sandbox mode, both FROM and TO must be verified.

5. 🔥 Launch Services
bash
Copy
Edit
docker compose up --build -d
6. 🧪 Test It!
Open your browser:

cpp
Copy
Edit
http://<YOUR_EC2_PUBLIC_IP>
Submit the feedback form.
📬 You should receive an email, and the message will be stored in the SQLite volume.

🗃️ Accessing Feedback Logs (Optional)
bash
Copy
Edit
docker compose exec feedback sqlite3 /data/feedback.db "SELECT * FROM feedback;"
📦 Build + Push Docker Images (Optional)
bash
Copy
Edit
docker build -t yourdockerhub/feedback feedback/
docker push yourdockerhub/feedback
🔐 Security & Best Practices
Never expose Flask or SQLite services publicly

Limit CORS in production to trusted origins

Use HTTPS for frontend (e.g., via Nginx + Let's Encrypt)

Store sensitive SMTP credentials using secrets or a secret manager

📈 Roadmap
 CI/CD pipeline via GitHub Actions

 Add admin dashboard to view feedback

 Store feedback in a cloud DB (RDS/DynamoDB)

 Integrate reCAPTCHA to prevent spam

📄 License
MIT License © 2025 Girish Hardia

yaml
Copy
Edit

---

## ✅ Want This in Your GitHub Now?

Just save this as `README.md` in your project root and push it:

```bash
git add README.md
git commit -m "Add professional README"
git push origin main
