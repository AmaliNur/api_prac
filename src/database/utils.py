from . import database


def get_db():
    db = database.SessionLocal()
    try:
        return db
    finally:
        db.close()
