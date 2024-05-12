from connection.connection_alq import db
from .entity_model import BaseModel

class AbstractPerson(BaseModel):
    __abstract__ = True
    # __tablename__ = 'abstract_persons'
    # id: Mapped[int] = mapped_column(Integer, primary_key=True)
    document_number = db.Column(db.String(15))
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String, nullable=False)
    phone = db.Column(db.String(15))
    address = db.Column(db.String(100))
    