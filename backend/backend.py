from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)


@app.route('/update/<count>')
def get_user_info(count):
    conn = psycopg2.connect(host='db',port=5432, user='example', password='example', dbname='count')
    cur = conn.cursor()
    sql = 'update count set num_count =' + count
    cur.execute(sql)
    conn.commit()
    conn.close()
    return jsonify({"count": count}), 200

@app.route("/get")
def get():
    conn = psycopg2.connect(host='db',port=5432, user='example', password='example', dbname='count')
    cur = conn.cursor()
    sql = 'select num_count from count'
    cur.execute(sql)
    row = cur.fetchone()
    conn.commit()
    conn.close()
    return jsonify({"count" : str(row[0])}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))


# docker build -t test .
# docker run -d --rm test1