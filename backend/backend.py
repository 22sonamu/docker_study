from flask import Flask, request, jsonify
import os

app = Flask(__name__)


@app.route('/update/<count>')
def get_user_info(count):
    return jsonify({"count": count}), 200

@app.route("/get")
def get():
    return "get"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))


# docker build -t test .
# docker run -d --rm test1