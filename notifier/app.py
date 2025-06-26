from flask import Flask, request
app = Flask(__name__)

@app.route('/notify', methods=['POST'])
def notify():
    data = request.json
    print(f" New Feedback Received:\nFrom: {data['name']}\nMessage: {data['message']}", flush=True)
    return {"status": "notified"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
