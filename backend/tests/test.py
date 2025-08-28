from httpx import AsyncClient
import pytest
from app.main import app


@pytest.mark.asyncio
async def test_version_endpoint():
    # Клиент для запросов к FastAPI (без запуска uvicorn)
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/api/version")

    # Проверяем, что сервер ответил
    assert response.status_code == 200

    # Проверяем, что в ответе есть ключ "version"
    json_data = response.json()
    assert "version" in json_data

