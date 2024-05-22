from pydantic import BaseModel, Field


class AuthorSchema(BaseModel):
    id: int
    name: str
