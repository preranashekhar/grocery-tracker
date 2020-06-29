from sqlalchemy.orm import Session

from database.models import *


def get_products(db: Session):
    return db.query(Product).all()
