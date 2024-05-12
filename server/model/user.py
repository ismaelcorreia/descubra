from datetime import datetime
from sqlalchemy import inspect, Enum
from .type_user import TypeUser
from connection.connection_alq import db
from .entity_model import BaseModel
from .abstract_person import AbstractPerson
from .empresa import Empresa


class User(db.Model, AbstractPerson, BaseModel):
    __tablename__ = 'users'
    # id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)

    type_user = db.Column(Enum(TypeUser), nullable=False)
    
    empresa_id = db.Column(db.String, db.ForeignKey("empresas.id"))
    empresa = db.relationship("Empresa")

    def to_dict(self):
        data = {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
        # Convert TypeUser enum to string
        if 'type_user' in data:
            data['type_user'] = data['type_user'].value
        if 'status' in data:
            data['status'] = data['status'].value
        # Format datetime objects as strings
        for key, value in data.items():
            if isinstance(value, datetime):
                data[key] = value.isoformat()

        return data
        # return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
