from datetime import datetime
from sqlalchemy import inspect, Enum
from connection.connection_alq import db
from .entity_model import BaseModel
from .abstract_person import AbstractPerson
# from .user import User


class Empresa(db.Model, AbstractPerson, BaseModel):
    __tablename__ = 'empresas'
    # id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    # nif = db.Column(db.String, unique=True, nullable=False)
    
    # users = db.relationship("User", back_populates='empresa')

    def to_dict(self):
        data = {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
        # Convert TypeUser enum to string
        if 'status' in data:
            data['status'] = data['status'].value
        # Format datetime objects as strings
        for key, value in data.items():
            if isinstance(value, datetime):
                data[key] = value.isoformat()

        return data
        # return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
