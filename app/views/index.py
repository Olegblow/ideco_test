import aiohttp_jinja2
from aiohttp import web
from json import JSONDecodeError

from utils import Service


class ServiseView(web.View):
    """ ."""
    service = Service('docker')

    @aiohttp_jinja2.template('index.html')
    async def get(self):
        context = {
            'is_active': await self.service.is_active,
            'service_name': self.service.service_name
         }
        return context

    async def post(self):
        functions = {
            'start': self.service.start,
            'stop': self.service.stop,
            'restart': self.service.restart
        }
        try:
            data = await self.request.json()
        except JSONDecodeError:
            response = {'status': 'bad request'}
            status = 400
        else:
            button = data.get('button')
            try:
                function = functions[button]
            except KeyError:
                response = {'status': 'request'}
                status = 400
            else:
                await function()
                response = {'status': 'ok'}
                status = 200
        return web.json_response(response, status=status)
