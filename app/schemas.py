from pydantic import BaseModel
from typing import List, Optional

class CategoryBase(BaseModel):
    title: str

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(CategoryBase):
    title: Optional[str] = None

class Category(CategoryBase):
    id: int

    class Config:
        from_attributes = True

class BookBase(BaseModel):
    title: str
    description: str
    price: float
    url: str = ""
    category_id: int

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    url: Optional[str] = None
    category_id: Optional[int] = None

class Book(BookBase):
    id: int

    class Config:
        from_attributes = True