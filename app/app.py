import os
import psycopg
from flask import Flask, jsonify
app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify(status="ok")

@app.get("/db-check")
def db_check():
    host = os.environ.get("DB_HOST", "localhost")
    port = os.environ.get("DB_PORT", "5432")
    try:
        with psycopg.connect(
            host=host,
            port=port,
            dbname=os.environ.get("DB_NAME", "campus"),
            user=os.environ.get("DB_USER", "campus"),
            password=os.environ.get("DB_PASSWORD", "dev-password"),
            connect_timeout=3,
        ) as conn:
            now = conn.execute("select now()").fetchone()[0]
        return jsonify(status="ok", db_host=host, now=str(now))
    except Exception as e:
        return jsonify(status="error", db_host=host, error=str(e)), 503

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)