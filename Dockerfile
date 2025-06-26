# 1. Start from official Python image
FROM python:3.10-slim

# 2. Set working directory inside container
WORKDIR /app

# 3. Copy all files from project folder to /app
COPY . .

# 4. Install dependencies
RUN apt-get update && \
    apt-get install -y sqlite3 && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# 5. Expose port 80 (for documentation, not enforcement)
EXPOSE 80

# 6. Run the Flask app when container starts
CMD ["python", "app.py"]
