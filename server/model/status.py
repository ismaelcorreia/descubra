from enum import Enum


class Status(Enum):
    ACTIVE = "ACTIVE",
    DISABLED = "DISABLED",
    DELETED = "DELETED",
    PAID = "PAID",
    PENDENT = "PENDENT",
    REFUSED = "REFUSED",

    # type_invoice_id = db.Column(db.Integer, db.ForeignKey("type_user"))
    # type_invoice = db.relationship("type_user")
