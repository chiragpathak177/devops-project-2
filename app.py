from flask import Flask
import os
import psycopg2

app = Flask(__name__)


@app.route("/")
def home():
    return "DevOps Project 2 - Application is running!"


@app.route("/db")
def database():
    try:
        connection = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        connection.close()
        return "Database connection successful!"
    except Exception as e:
        return f"Database connection failed: {e}", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)