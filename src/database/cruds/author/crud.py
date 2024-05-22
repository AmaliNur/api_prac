from sqlalchemy.orm import Session
from fastapi.params import Depends

from ....database.models.author import Authors
from ...utils import get_db
from ....logger import setup_logger


setup_logger('api-author-crud')


class AuthorCRUD:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def find_one(self, **kwargs) -> Authors | None:
        query = self.db.query(Authors)
        return query.filter_by(**kwargs).first()
