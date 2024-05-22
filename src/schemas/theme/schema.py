import random

from pydantic import BaseModel, Field


def get_r():
    return random.randint(1, 100000)


class ThemeSchema(BaseModel):
    id: int = Field(default_factory=get_r)
    name: str
