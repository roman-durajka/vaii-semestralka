from flask import Flask, request, session
from shop.models import Product

app = Flask(__name__)


@app.route('/shop/cart/stock')
def product_quantity():
    message = ""
    for product_id, data in session["cart"].items():
        db_item = Product.objects.get(id=product_id)
        if db_item["stock"] < data["quantity"]:
            message += f"Item {data['name']} does not have enough stock! There are {db_item['stock']} available pieces.\n"

    return {"message": message}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
