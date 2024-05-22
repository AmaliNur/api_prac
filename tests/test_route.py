from fastapi.testclient import TestClient
from ..src.main import app


client = TestClient(app)


def test_comment_create():
    response = client.post('comment/506', json={
        "theme_id": 50,
        "author_id": 100,
        "quote_id": 0,
        "comment_text": "test"
    })
    assert "Такой темы нет" in response.text


def test_comment_get_by_theme():
    response = client.get('comment/50')
    assert "Такой темы нет" in response.text


def test_comment_get():
    response = client.get('comment/comment/47909')
    assert response.json()['id'] == 47909


def test_themes_all():
    response = client.get('theme/')
    assert type(response.json()) == list


def test_themes_create():
    response = client.post('theme/', json={
        'name': 'Приветики'
    })
    assert response.json()['name'] == 'Приветики'


def test_theme_get_by_id():
    response = client.get('theme/602')
    assert response.json()['id'] == 602


def test_theme_delete():
    response = client.delete('theme/60048')
    assert "Темы с таким айди нет" in response.text
