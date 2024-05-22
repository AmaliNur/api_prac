from typing import Annotated, List
from fastapi import APIRouter, Depends, HTTPException, Body

from ...schemas.comment.schema import CommentSchema, CommentEdit
from ...database.cruds.comment.crud import CommentCRUD
from ...database.cruds.theme.crud import ThemeCRUD
from ...database.cruds.author.crud import AuthorCRUD
from ...logger import setup_logger


setup_logger('api-comment-router')

router = APIRouter(prefix='/comment', tags=['comment'])


@router.post('/{theme_id}', response_model=CommentSchema)
async def create_comment(theme_id: int,
                         content: Annotated[CommentSchema, Body()],
                         db_comment: CommentCRUD = Depends(),
                         db_theme: ThemeCRUD = Depends()):
    """Endpoint для создания нового комментария.
    На вход принимает id темы для привязки и данные для полей"""
    db_theme_data = db_theme.find_one(id=theme_id)

    if not db_theme_data:
        raise HTTPException(status_code=400, detail={"error": "Такой темы нет"})

    if content.quote_id:
        if not db_comment.find_one(id=content.quote_id):
            raise HTTPException(status_code=400, detail={"error": "No such quote"})

    content.theme_id = theme_id
    result = db_comment.create(content)
    return result


@router.get('/{theme_id}', response_model=List[CommentSchema])
async def get_comments(theme_id: int,
                       db_comment: CommentCRUD = Depends(),
                       db_theme: ThemeCRUD = Depends()):
    """Endpoint, возвращающий все комментарии темы по ее айди"""
    db_theme_data = db_theme.find_one(id=theme_id)

    if not db_theme_data:
        raise HTTPException(status_code=400, detail={"error": "Такой темы нет"})

    result = db_comment.find_all(theme_id=theme_id)
    return result


@router.get('/comment/{comment_id}', response_model=CommentSchema)
async def get_comment(comment_id: int,
                      db_comment: CommentCRUD = Depends()):
    """Endpoint для получения комментария по его id"""
    result = db_comment.find_one(id=comment_id)
    if not result:
        raise HTTPException(status_code=400, detail={"error": "Такого коммента нет"})
    return result


@router.put('/{comment_id}', response_model=CommentSchema)
async def update_comment(comment_id: int,
                         content: Annotated[CommentEdit, Body()],
                         db_comment: CommentCRUD = Depends(),
                         db_author: AuthorCRUD = Depends()):
    if content.quote_id:
        if not db_comment.find_one(id=content.quote_id):
            raise HTTPException(status_code=400, detail={"error": "No such quote"})

    if not db_comment.find_one(id=comment_id):
        raise HTTPException(status_code=400, detail={"error": "No such comment"})

    if not db_author.find_one(id=content.author_id):
        raise HTTPException(status_code=400, detail={"error": "No such author"})

    content.id = comment_id
    db_comment.update(**content.dict())
    return content
