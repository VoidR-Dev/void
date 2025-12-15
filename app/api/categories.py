from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.db import get_db
from app.db.crud import create_category, read_category, read_all_categories, update_category, delete_category
from app.schemas import CategoryCreate, CategoryUpdate, Category

router = APIRouter(prefix="/categories", tags=["categories"])

@router.post("/", response_model=Category, status_code=status.HTTP_201_CREATED)
def create(category: CategoryCreate, db: Session = Depends(get_db)):
    return create_category(db, category.title)

@router.get("/", response_model=List[Category])
def read_all(db: Session = Depends(get_db)):
    return read_all_categories(db)

@router.get("/{category_id}", response_model=Category)
def read(category_id: int, db: Session = Depends(get_db)):
    category = read_category(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.put("/{category_id}", response_model=Category)
def update(category_id: int, category: CategoryUpdate, db: Session = Depends(get_db)):
    updated = update_category(db, category_id, category.title)
    if not updated:
        raise HTTPException(status_code=404, detail="Category not found")
    return updated

@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(category_id: int, db: Session = Depends(get_db)):
    deleted = delete_category(db, category_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Category not found")