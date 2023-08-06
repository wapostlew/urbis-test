import asyncio
import pytest

from fastapi.testclient import TestClient
from httpx import AsyncClient

from app.apps.user import models


class TestModel:

    @pytest.mark.anyio
    async def test_mock_databases(self, client_test: AsyncClient):
        await models.User(
            name="Waldemar",
            surname="Apostle"
        ).create()