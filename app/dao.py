import json

def load_categories():
    with open("data/category.json", encoding="utf-8") as f:
        return json.load(f)

def load_product(category_id=None, q=None):
    with open("data/product.json", encoding="utf-8") as f:
        products = json.load(f)
        if q:
            products = [p for p in products if p["name"].find(q)]

        if category_id:
            products = [p for p in products if p["cate_id"]==category_id]
        return products

def get_product_by_id(id):
    with open("data/product.json", encoding="utf-8") as f:
        product = json.load(f)
        product = [p for p in product if p.id == id]
        return product