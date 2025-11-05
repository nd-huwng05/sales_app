import json

from sqlalchemy.orm import relationship

from app import db, app
from sqlalchemy import Column,INTEGER, String, Float, ForeignKey

class Category(db.Model):
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    name = Column(String(150), nullable=False, unique=True)
    products = relationship('Product', backref="category", lazy=True)

    def __str__(self):
        return self.name

class Product(db.Model):
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    name = Column(String(150), nullable=False, unique=True)
    image = Column(String(300), default="https://cdnv2.tgdd.vn/mwg-static/common/News/1582589/12-l%20%282%29.jpg")
    price = Column(Float, default=0.0)
    cate_id = Column(INTEGER, ForeignKey(Category.id), nullable=False)

if __name__ == "__main__":
    with app.app_context():
        # db.create_all()
        # cate = ["Laptop", "Tablet", "Phone"]
        # for c in cate:
        #     db.session.add(Category(name=c))
        # db.session.commit()

        with open("data/product.json", encoding="utf-8") as f:
            products = json.load(f)

            for p in products:
                db.session.add(Product(**p))
            db.session.commit()