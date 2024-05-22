from typing import Annotated, List
from fastapi import APIRouter, Depends, HTTPException, Body

from ...schemas.theme.schema import ThemeSchema
from ...database.cruds.theme.crud import ThemeCRUD
from ...logger import setup_logger


setup_logger('api-theme-router')

router = APIRouter(prefix='/theme', tags=['theme'])


@router.post('/', response_model=ThemeSchema)
async def create_theme(content: Annotated[ThemeSchema, Body()],
                       db_theme: ThemeCRUD = Depends()):
    """Endpoint для создания новой темы"""

    result = db_theme.create(content)
    return result


@router.get('/', response_model=List[ThemeSchema])
async def all_themes(db_theme: ThemeCRUD = Depends()):
    """Endpoint для получения всех тем"""

    result = db_theme.find_all()
    return result


@router.get('/{theme_id}', response_model=ThemeSchema)
async def get_theme(theme_id: int,
                    db_theme: ThemeCRUD = Depends()):
    """Endpoint для получения темы по ее ID"""

    result = db_theme.find_one(id=theme_id)
    if not result:
        raise HTTPException(status_code=400, detail={"error": "Темы с таким айди нет"})
    return result


@router.delete('/{theme_id}', response_model=ThemeSchema)
async def delete_theme(theme_id: int,
                       db_theme: ThemeCRUD = Depends()):
    """Endpoint для удаления темы по ID"""
    result = db_theme.find_one(id=theme_id)
    if not result:
        raise HTTPException(status_code=400, detail={"error": "Темы с таким айди нет"})
    db_theme.delete(id=theme_id)
    return result
