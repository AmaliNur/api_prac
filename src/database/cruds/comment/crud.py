from typing import Type
from sqlalchemy.orm import Session
from fastapi.params import Depends

from ....database.models.comment import Comments
from ....schemas.comment.schema import CommentSchema
from ...utils import get_db
from ....logger import setup_logger


setup_logger('api-comment-crud')


class CommentCRUD:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def create(self, data: CommentSchema) -> Comments:
        data = Comments(**data.dict())
        self.db.add(data)
        self.db.commit()
        self.db.refresh(data)
        return data

    def find_one(self, **kwargs) -> Comments | None:
        query = self.db.query(Comments)
        return query.filter_by(**kwargs).first()

    def find_all(self, **kwargs) -> list[Type[Comments]]:
        query = self.db.query(Comments)
        return query.filter_by(**kwargs).all()

    def update(self, **data) -> None:
        id = data['id']
        del data['id']
        query = self.db.query(Comments)
        query.filter_by(id=id).update(**data)
        self.db.commit()
