import math

from flask import render_template, request
import dao
from app import app


@app.route("/")
def index():
    q = request.args.get("q")
    # products = dao.load_product(q = q)
    pages = math.ceil(dao.count_product() / app.config["SIZE_PAGES"])

    page = request.args.get("page")
    products = dao.load_product(page=page)
    return render_template("index.html", products=products, pages=int(pages))

@app.route("/product")
def get_data():
    category_id = request.args.get("cates_id")
    products = math.ceil(dao.load_product(category_id = int(category_id)))
    return render_template("index.html", products=products)

@app.route("/products/<int:id>")
def details(id):
    product = dao.get_product_by_id(id=int(id))
    return render_template("detail.html", prod=product)


@app.context_processor
def common_attribute():
    return {
        "cates": dao.load_categories()
    }

if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)