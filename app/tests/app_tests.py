from app import init_app
from utils import Service

import pytest


@pytest.fixture
async def client(test_client):
    """Создаем фикстуру клиента."""
    app = init_app()
    return await test_client(app)


async def test_get_views_status(client):
    """Проверяем статус get запроса основноо урла"""
    resp = await client.get('/')
    assert resp.status == 200


@pytest.mark.parametrize(
    'parameters',
    (
        # body status
        ({}, 400),
        ({"button": ""}, 400),
        ({"button": "start"}, 200)
    )
)
async def test_post_views_status(client, parameters):
    """Проверяем post запроссы. """
    data, status = parameters
    resp = await client.post('/', json=data)
    assert resp.status == status


@pytest.mark.asyncio
async def test_service_class():
    """Проверяем работоспособность класса Service."""
    service = Service('docker')
    name = service.service_name
    assert name == 'docker'
    is_active = await service.is_active
    assert is_active in (True, False)
    await service.stop()
    stop_is_active = await service.is_active
    assert stop_is_active is False
    await service.start()
    start_is_active = await service.is_active
    assert start_is_active is True
    await service.restart()
    restart_is_active = await service.is_active
    assert restart_is_active is True


@pytest.mark.parametrize(
    'parameters',
    (
        # body status
        ({}, 400),
        ({"is_flagged": ""}, 400),
        ({"is_flagged": "yes"}, 200),
        ({"is_flagged": "no"}, 200)
    )
)
async def test_redis_view(client, parameters):
    """Тест проверки ответов от вьюхи установление флага."""
    data, status = parameters
    response = await client.post('/redis', json=data)
    assert response.status == status
