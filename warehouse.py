from app import app
from flask import jsonify
from db import conn

@app.route("/warehouses")

def get_warehouses():

    cur=conn.cursor()

    cur.execute("SELECT * FROM warehouses")

    rows=cur.fetchall()

    cur.close()

    return jsonify(rows)