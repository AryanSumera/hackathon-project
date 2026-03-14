from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

import routes.products
import routes.receipts
import routes.deliveries
import routes.inventory
import routes.moves
import routes.warehouse

@app.route("/")
def home():
    return {"message":"CoreInventory API running"}

if __name__ == "__main__":
    app.run(debug=True)