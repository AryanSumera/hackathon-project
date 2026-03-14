from app import app
from flask import request, jsonify
from db import conn

@app.route("/products", methods=["GET"])
def get_products():

    cur = conn.cursor()
    cur.execute("SELECT * FROM products")
    rows = cur.fetchall()
    cur.close()

    return jsonify(rows)


@app.route("/products", methods=["POST"])
def add_product():

    data = request.json

    cur = conn.cursor()

    cur.execute(
        "INSERT INTO products (name,sku,unit) VALUES (%s,%s,%s)",
        (data["name"],data["sku"],data["unit"])
    )

    conn.commit()
    cur.close()

    return {"message":"product added"}