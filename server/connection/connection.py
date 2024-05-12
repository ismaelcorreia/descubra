from src.app import app
import os


# app.config["SQLALCHEMY_DATABASE_URI"] = "dialect://username:password@host:port/database"
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@1234@localhost:3306/db_spake"

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get()
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db_spake.db"