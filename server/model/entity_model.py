from sqlalchemy import inspect
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, UTC
from connection.connection_alq import db
from sqlalchemy import Enum
from model.status import Status
Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True
    # id = db.Column(db.String(50), primary_key=True, unique=True, nullable=False)
    id = db.Column(db.String(50), primary_key=True, unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(UTC))
    updated_at = db.Column(db.DateTime, default=datetime.now(UTC), onupdate=datetime.now(UTC))

    status = db.Column(Enum(Status), nullable=False, default="ACTIVE")

    def to_dict(self):
        data = {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
        if 'status' in data:
            data['status'] = data['status'].value
        # Format datetime objects as strings
        for key, value in data.items():
            if isinstance(value, datetime):
                data[key] = value.isoformat()

        return data
        # return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
    
    