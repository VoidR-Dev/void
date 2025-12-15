from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional

from app.db.db import get_db
from app.db.crud import create_book, read_book, read_all_books, update_book, delete_book, read_category
from app.schemas import BookCreate, BookUpdate, Book

router = APIRouter(prefix="/books", tags=["books"])

@router.post("/", response_model=Book, status_code=status.HTTP_201_CREATED)
def create(book: BookCreate, db: Session = Depends(get_db)):
    if not read_category(db, book.category_id):
        raise HTTPException(status_code=404, detail="Category not found")
    return create_book(db, book.title, book.description, book.price, book.url, book.category_id)

@router.get("/", response_model=List[Book])
def read_all(category_id: Optional[int] = None, db: Session = Depends(get_db)):
    books = read_all_books(db)
    if category_id:
        books = [b for b in books if b.category_id == category_id]
    return books

@router.get("/{book_id}", response_model=Book)
def read(book_id: int, db: Session = Depends(get_db)):
    book = read_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.put("/{book_id}", response_model=Book)
def update(book_id: int, book: BookUpdate, db: Session = Depends(get_db)):
    if book.category_id and not read_category(db, book.category_id):
        raise HTTPException(status_code=404, detail="Category not found")
    updated = update_book(db, book_id, book.title, book.description, book.price, book.url, book.category_id)
    if not updated:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(book_id: int, db: Session = Depends(get_db)):
    deleted = delete_book(db, book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Book not found")