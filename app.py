from flask import Flask, send_file

app = Flask(__name__)


@app.route("/")
def home():
    return send_file("webapp.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
