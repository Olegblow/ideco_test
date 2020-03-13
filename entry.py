import asyncio
from aiohttp import web
from app.app import init_app
import uvloop


asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


def main():
    app = init_app()
    web.run_app(app, host='localhost', port='8080')


if __name__ == '__main__':
    main()