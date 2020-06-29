from fastapi import Depends, FastAPI
from typing import List, Optional
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import models
from database.base import SessionLocal, engine
import database.db_endpoints as dbe

# creating db tables
models.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()


class Brand(BaseModel):
    name: str

    class Config:
        orm_mode = True


class Product(BaseModel):
    name: str
    variety_id: Optional[int] = None
    brand_id: Optional[int] = None
    brand: Brand

    class Config:
        orm_mode = True


@app.get("/products", response_model=List[Product])
def get_products(db: Session = Depends(get_db)):
    res = dbe.get_products(db)
    print("res: ", res)
    return dbe.get_products(db)
