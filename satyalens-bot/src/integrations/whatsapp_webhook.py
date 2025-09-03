from flask import Flask, request

app = Flask(__name__)

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    # verification for GET, message handling for POST
    return "OK", 200

if __name__ == "__main__":
    app.run(port=5000)
