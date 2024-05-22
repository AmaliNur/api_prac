from typing import Type
from sqlalchemy.orm import Session
from fastapi import Depends

from ....database.models.theme import Theme
from ....schemas.theme.schema import ThemeSchema
from ...utils import get_db
from ....logger import setup_logger


setup_logger('api-theme-crud')


class ThemeCRUD:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def create(self, data: ThemeSchema) -> Theme:
        data = Theme(**data.dict())
        self.db.add(data)
        self.db.commit()
        self.db.refresh(data)
        return data

    def find_one(self, **kwargs) -> Theme | None:
        query = self.db.query(Theme)
        return query.filter_by(**kwargs).first()

    def find_all(self, **kwargs) -> list[Type[Theme]]:
        query = self.db.query(Theme)
        return query.filter_by(**kwargs).all()

    def delete(self, **kwargs) -> None:
        query = self.db.query(Theme)
        query.filter_by(**kwargs).delete()
        self.db.commit()
