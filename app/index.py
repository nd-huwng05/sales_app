from flask import Flask, render_template, request
import dao

app = Flask(__name__)

@app.route("/")
def index():
    q = request.args.get("q")
    cates = dao.load_categories()
    products = dao.load_product(q = q)
    return render_template("index.html", products=products)

@app.route("/product")
def get_data():
    category_id = request.args.get("cates_id")
    cates = dao.load_categories()
    products = dao.load_product(category_id = int(category_id))
    return render_template("index.html", products=products)

@app.route("/products/<int:id>")
def details(id):

    return render_template("detail.html")


@app.context_processor
def common_attribute():
    return {
        "cates": dao.load_categories()
    }

if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)