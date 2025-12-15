from sqlalchemy.orm import Session
from .models import Category, Book
from typing import Optional

def create_category(db: Session, title: str):
    db_category = Category(title=title)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def read_category(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()

def read_all_categories(db: Session):
    return db.query(Category).all()

def update_category(db: Session, category_id: int, title: str):
    db_category = read_category(db, category_id)
    if db_category:
        db_category.title = title
        db.commit()
        db.refresh(db_category)
    return db_category

def delete_category(db: Session, category_id: int):
    db_category = read_category(db, category_id)
    if db_category:
        db.delete(db_category)
        db.commit()
    return db_category

def create_book(db: Session, title: str, description: str, price: float, url: str, category_id: int):
    db_book = Book(title=title, description=description, price=price, url=url, category_id=category_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def read_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def read_all_books(db: Session):
    return db.query(Book).all()

def update_book(db: Session, book_id: int, title: Optional[str] = None, description: Optional[str] = None, price: Optional[float] = None, url: Optional[str] = None, category_id: Optional[int] = None):
    db_book = read_book(db, book_id)
    if db_book:
        if title is not None: db_book.title = title
        if description is not None: db_book.description = description
        if price is not None: db_book.price = price
        if url is not None: db_book.url = url
        if category_id is not None: db_book.category_id = category_id
        db.commit()
        db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int):
    db_book = read_book(db, book_id)
    if db_book:
        db.delete(db_book)
        db.commit()
    return db_book