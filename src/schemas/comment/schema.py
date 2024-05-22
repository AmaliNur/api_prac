import random

from pydantic import BaseModel, Field


def get_r():
    return random.randint(1, 100000)


class CommentSchema(BaseModel):
    id: int = Field(default_factory=get_r)
    theme_id: int | None = Field(None)
    author_id: int
    quote_id: int | None = Field(None)
    comment_text: str


class CommentEdit(BaseModel):
    id: int
    author_id: int
    comment_text: str
    quote_id: int = Field(None)
