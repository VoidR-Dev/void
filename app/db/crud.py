from sqlalchemy.orm import Session
from .models import Category, Book

# === Categories CRUD ===
def create_category(db: Session, title: str):
    db_category = Category(title=title)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_category(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()

def get_categories(db: Session):
    return db.query(Category).all()

# === Books CRUD ===
def create_book(db: Session, title: str, description: str, price: float, url: str, category_id: int):
    db_book = Book(title=title, description=description, price=price, url=url, category_id=category_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session):
    return db.query(Book).all()

def get_books_by_category(db: Session, category_id: int):
    return db.query(Book).filter(Book.category_id == category_id).all()
