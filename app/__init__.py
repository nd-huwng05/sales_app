from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@localhost/salesdb?charset=utf8mb4"
app.config["SIZE_PAGES"] = 2
db = SQLAlchemy(app)
