from db.db import engine, Base
from db.models import Category, Book
from db.crud import create_category, create_book
from db.db import SessionLocal

# Создаём таблицы
Base.metadata.create_all(bind=engine)

db = SessionLocal()

# Добавляем категории
fantasy = create_category(db, "Фэнтези")
detective = create_category(db, "Детектив")

# Книги в Фэнтези
create_book(db, "Властелин колец", "Эпическая сага о кольце", 1290.0, "", fantasy.id)
create_book(db, "Игра престолов", "Политика и драконы", 990.0, "", fantasy.id)
create_book(db, "Гарри Поттер и философский камень", "Мальчик-волшебник", 790.0, "", fantasy.id)

# Книги в Детективе
create_book(db, "Убийство в Восточном экспрессе", "Классика Агаты Кристи", 650.0, "", detective.id)
create_book(db, "Девушка с татуировкой дракона", "Скандинавский нуар", 890.0, "", detective.id)

print("База данных успешно инициализирована!")
db.close()
