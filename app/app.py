import asyncio
from aiohttp import web
from .routes import setup_routes


async def init_app() -> web.Application:
    """Инициализирует web приложение."""
    app = web.Application()
    setup_routes(app)
    return app
