from app import app
from flask import request
from db import conn

@app.route("/moves", methods=["POST"])

def add_move():

    data=request.json

    cur=conn.cursor()

    cur.execute(
    "INSERT INTO moves (product_id,source_warehouse,destination_warehouse,quantity) VALUES (%s,%s,%s,%s)",
    (data["product_id"],data["source"],data["destination"],data["quantity"])
    )

    conn.commit()
    cur.close()

    return {"message":"move recorded"}