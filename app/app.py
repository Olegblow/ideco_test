import asyncio
import pathlib
import uvloop

import aiohttp_jinja2
import jinja2
from aiohttp import web

from routes import setup_routes


asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
TEMPLATES_ROOT = pathlib.Path(__file__).parent / 'templates'


def init_app() -> web.Application:
    """Инициализирует web приложение."""
    app = web.Application()
    setup_routes(app)
    return app


def setup_jinja(app: web.Application) -> None:
    """Сетапим jinja2."""
    loader = jinja2.FileSystemLoader(str(TEMPLATES_ROOT))
    aiohttp_jinja2.setup(app, loader=loader)


def main():
    app = init_app()
    setup_jinja(app)
    web.run_app(app, host='0.0.0.0', port='8080')


if __name__ == '__main__':
    main()
