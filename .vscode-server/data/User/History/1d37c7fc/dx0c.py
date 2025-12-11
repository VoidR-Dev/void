from db.db import SessionLocal
from db.crud import get_categories, get_books
from db.models import Category, Book

db = SessionLocal()

print("=== Категории ===")
for cat in get_categories(db):
    print(f"{cat.id}. {cat.title}")

print("\n=== Все книги ===")
for book in get_books(db):
    print(f"[{book.category.title}] {book.title} — {book.price} руб.")

db.close()
