import os

from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)


def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )


@app.route("/")
def home():
    return jsonify({"message": "ShopSphere API is running"})


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


@app.route("/api/products")
def products():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT id, name, price FROM products")
    products = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(products)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
