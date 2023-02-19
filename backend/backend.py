from flask import Flask, request, jsonify
import pymysql
import os

app = Flask(__name__)



@app.route('/update/<count>')
def get_user_info(count):
    return jsonify({"count": count}), 200

@app.route("/get")
def get():
    conn = pymysql.connect(host='127.0.0.1',port=5432, user='example', password='example', db='count', charset='utf8')
    cur = conn.cursor()
    sql = 'select * from count'
    cur.execute(sql)
    row = cur.fetchone()
    conn.commit()
    conn.close()
    return row[0]

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))


# docker build -t test .
# docker run -d --rm test1