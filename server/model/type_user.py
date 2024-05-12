from enum import Enum
# from sqlalchemy import inspect
# from ..connection.connection_alq import db
# from .entity_model import BaseModel
#
# class TypeUser(db.Model, BaseModel):
#     __tablename__ = 'type_users'
#     # id = db.Column(db.Integer, primary_key=True)
#     description = db.Column(db.Text, nullable=False)
#
#     users = db.relationship('User', back_populates='type_user')
#
#     def to_dict(self):
#         return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }


class TypeUser(Enum):
    ADMIN = "ADMIN"
    USER = "USER"
    MANAGER = "MANAGER"


