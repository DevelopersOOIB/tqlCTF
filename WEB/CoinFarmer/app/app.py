from flask import Flask, session, render_template, redirect, request
import json


app = Flask(__name__)
app.secret_key = 'lollypop123'


def load_products():
    with open('products.json') as f:
    	products = json.loads(f.read())
    return products["products"]


@app.route('/', methods=["GET"])
def index():
    if not session:
        session['coins'] = 0
        session['products'] = []
    return render_template('index.html', session=session)


@app.route('/orders', methods=["GET"])
def own():
    if not session:
        return redirect('/')
    return render_template('orders.html', session=session)


@app.route('/farm_coin', methods=["GET", "POST"])
def click_coin():
    if request.method == "POST":
        if not session:
            return redirect('/')
        session["coins"] += 1
    return redirect('/')


@app.route('/shop', methods=["GET"])
def shop():
    if not session:
        return redirect('/')
    
    products = load_products()
    return render_template('shop.html', products=products)


@app.route('/buy/<id>', methods=["GET"])
def buy(id):
    if not session:
        return redirect('/')
    
    products = load_products()
    product = {}

    if "products" not in session:
        session["products"] = []

    for i in products:
        if str(i["id"]) == id:
            product = i

    if not product:
        return redirect('/')
    
    current_balance = session["coins"]
    
    if product in session["products"]:
        return render_template("already_have.html", product=product) 
    
    if current_balance < product["price"]:
        return render_template("no_money.html", product=product)
    
    session["coins"] = current_balance - product["price"]
    session["products"].append(product)
    return render_template('success.html', product=product)
    


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")

