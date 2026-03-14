from app import app
from flask import request
from db import conn

@app.route("/deliveries", methods=["POST"])
def add_delivery():

    data = request.json

    product_id = data["product_id"]
    warehouse_id = data["warehouse_id"]
    quantity = data["quantity"]

    cur = conn.cursor()

    # insert delivery
    cur.execute(
        "INSERT INTO deliveries (product_id,warehouse_id,quantity) VALUES (%s,%s,%s)",
        (product_id,warehouse_id,quantity)
    )

    # update inventory
    cur.execute(
        """
        UPDATE inventory
        SET on_hand = on_hand - %s,
            free_to_use = free_to_use - %s
        WHERE product_id=%s AND warehouse_id=%s
        """,
        (quantity,quantity,product_id,warehouse_id)
    )

    conn.commit()
    cur.close()

    return {"message":"delivery added"}