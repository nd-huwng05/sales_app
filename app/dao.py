import json

from app import app
from app.models import Product, Category


def load_categories():
    return  Category.query.all()

def load_product(category_id=None, q=None, page=1):
        if q:
            return Product.query.where("name like ?", q).all()

        if category_id:
            return Product.query.where("cate_id = ?", category_id).all()

        if page:
            start = (int(page)-1)*app.config['SIZE_PAGES']
            end = start + app.config['SIZE_PAGES']
            return Product.query.slice(start, end)

        return Product.query.all()


def count_product():
    return Product.query.count()

def get_product_by_id(id):
    return Product.query.get(id)