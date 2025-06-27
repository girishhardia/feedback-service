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

## 🚀 How to Run

### 1. 🐳 Install Docker (if not already):

```bash
sudo yum install docker -y
sudo service docker start
```

---

### 2. 📦 Install Docker Compose Plugin

If `docker compose` isn't available:

```bash
sudo curl -L https://github.com/docker/compose/releases/download/v2.24.6/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

---

Here's the provided content converted into a **GitHub README markdown format**:

-----

## 🛠️ Clone the Project

To get started, clone the repository and navigate into the project directory:

```bash
git clone https://github.com/your-username/feedback-service.git
cd feedback-service
```

-----

## ⚙️ Add Environment Variables

Create a file named `.env` inside the `notifier/` directory with the following content. **Remember to replace the placeholder values with your actual credentials.**

```env
SMTP_USERNAME=your-smtp-username
SMTP_PASSWORD=your-smtp-password
SMTP_SERVER=email-smtp.us-east-1.amazonaws.com
SMTP_PORT=587
TO_EMAIL=you@example.com
FROM_EMAIL=verified@yourdomain.com
```

🔐 **Note:** If your SES (Simple Email Service) is in sandbox mode, both `FROM_EMAIL` and `TO_EMAIL` must be verified in SES.

-----

## 🔥 Launch Services

Once your environment variables are set, launch the services using Docker Compose:

```bash
docker compose up --build -d
```

-----

## 🧪 Test It\!

Open your web browser and visit the following URL, replacing `<YOUR_EC2_PUBLIC_IP>` with the public IP address of your EC2 instance:

```
http://<YOUR_EC2_PUBLIC_IP>
```

Fill out the feedback form.

📬 You should receive an email with the submitted feedback.

🗃️ The message will also be stored in the SQLite volume.

-----

## 🗃️ Accessing Feedback Logs (Optional)

To view the feedback messages stored in the SQLite database, you can execute the following command:

```bash
docker compose exec feedback sqlite3 /data/feedback.db "SELECT * FROM feedback;"
```

-----

## 📦 Build + Push Docker Images (Optional)

If you wish to build and push your Docker images to a registry (like Docker Hub), use these commands:

```bash
docker build -t yourdockerhub/feedback feedback/
docker push yourdockerhub/feedback
```

-----

## 🔐 Security & Best Practices

Here are some important security considerations and best practices:

  * ❌ **Never expose Flask or SQLite services publicly.** These should only be accessible internally or through a secure reverse proxy.
  * ✅ **Limit CORS in production to trusted origins.** Configure your Cross-Origin Resource Sharing (CORS) settings to only allow requests from known and trusted domains.
  * ✅ **Use HTTPS for frontend.** Implement HTTPS for your frontend (e.g., via Nginx with Let's Encrypt) to encrypt communication.
  * ✅ **Store SMTP credentials securely.** Avoid hardcoding sensitive credentials. Instead, use secure methods like GitHub Secrets or AWS Secrets Manager.

-----

## 📈 Roadmap

Here's what's planned for future development:

  * CI/CD pipeline via GitHub Actions
  * Add an admin dashboard to view feedback
  * Store feedback in a cloud database (e.g., RDS/DynamoDB)
  * Integrate reCAPTCHA to prevent spam

-----

## 📄 License

MIT License © 2025 Girish Hardia

-----

![image](https://github.com/user-attachments/assets/f509d31e-b178-4726-8979-778b31dcef23)

![Untitled](https://github.com/user-attachments/assets/b9af41ef-192c-4a36-bbb9-9c0705c0277f)
