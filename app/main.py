from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.db.db import get_db, engine
from app.api.categories import router as categories_router
from app.api.books import router as books_router

app = FastAPI(title="Book API")

app.include_router(categories_router)
app.include_router(books_router)

@app.get("/health")
def health(db: Session = Depends(get_db)):
    return {"status": "healthy", "db_connection": "ok"}

@app.on_event("startup")
def startup():
    with engine.connect() as connection:
        pass

@app.get("/")
def root():
    return {"message": "Book API is running"}

