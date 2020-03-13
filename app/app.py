import asyncio
from aiohttp import web
from .routes import setup_routes


async def init_app() -> web.Application:
    """Инициализирует web приложение."""
    app = web.Application()
    print('init.routec')
    setup_routes(app)
    print(app.router)
    return app
