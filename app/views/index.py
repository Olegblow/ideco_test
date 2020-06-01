import aiohttp_jinja2
from aiohttp import web

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
        data = await self.request.json()
        button = data.get('button')
        response = {'status': 'ok'}
        functions = {
            'start': self.service.start,
            'stop': self.service.stop,
            'restart': self.service.restart
        }
        function = functions[button]
        await function()
        return web.json_response(response)
