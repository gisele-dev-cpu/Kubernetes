from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "ShopSphere API is running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/api/products")
def products():
    return jsonify([
        {
            "id": 1,
            "name": "Laptop",
            "price": 999.99
        },
        {
            "id": 2,
            "name": "Headphones",
            "price": 149.99
        },
        {
            "id": 3,
            "name": "Keyboard",
            "price": 79.99
        }
    ])


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
