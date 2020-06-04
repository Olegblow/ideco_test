import aiohttp_jinja2
from aiohttp import web
import aioredis
from json import JSONDecodeError

from utils import Service


class ServiseView(web.View):
    """Оснавная view для работы с сервисом."""
    service = Service('docker')

    @aiohttp_jinja2.template('index.html')
    async def get(self):
        flagged_status = {
            'yes': True,
            'no': False,
        }
        connect = await aioredis.create_redis_pool(('localhost', 6379))
        is_flagged = flagged_status.get(
            await connect.get('is_flagged', encoding='utf-8'),
            False
        )
        connect.close()
        await connect.wait_closed()
        context = {
            'is_active': await self.service.is_active,
            'service_name': self.service.service_name,
            'is_flagged': is_flagged
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
                response = {'status': 'bad request'}
                status = 400
            else:
                await function()
                response = {'status': 'ok'}
                status = 200
        return web.json_response(response, status=status)


async def redis_view(request):
    """Вьюха принемает значения флага и устанавливает его в редис."""
    flagged_status = ('yes', 'no')
    try:
        data = await request.json()
    except JSONDecodeError:
        response = {'status': 'bad request'}
        status = 400
    else:
        is_flagged = data.get('is_flagged')
        if is_flagged in flagged_status:
            connect = await aioredis.create_redis_pool(('localhost', 6379))
            await connect.set('is_flagged', is_flagged )
            connect.close()
            await connect.wait_closed()
            response = {'status': 'ok'}
            status = 200
        else:
            response = {'status': 'bad request'}
            status = 400
    return web.json_response(response, status=status)

