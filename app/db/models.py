from sqlalchemy import ForeignKey, String, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from .db import Base

class Category(Base):
    __tablename__ = "categories"   
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, unique=True, index=True)
    books: Mapped[List["Book"]] = relationship("Book", back_populates="category")

class Book(Base):
    __tablename__ = "books"        

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, index=True)
    description: Mapped[str] = mapped_column(String)
    price: Mapped[float] = mapped_column(Float)
    url: Mapped[str] = mapped_column(String, default="")
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    category: Mapped["Category"] = relationship("Category", back_populates="books")