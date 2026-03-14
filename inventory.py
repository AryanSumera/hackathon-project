from app import app
from flask import jsonify
from db import conn

@app.route("/inventory")

def get_inventory():

    cur=conn.cursor()

    cur.execute("SELECT * FROM inventory")

    rows=cur.fetchall()

    cur.close()

    return jsonify(rows)