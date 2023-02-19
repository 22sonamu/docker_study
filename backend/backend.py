from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def index():
    return 'Hellow World'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
# docker build -t test .
# docker run -d --rm test1