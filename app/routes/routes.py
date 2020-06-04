from views import ServiseView
from views import redis_view


def setup_routes(app):
    """Создаем маршруты приложения."""
    app.router.add_route('*', '', ServiseView)
    app.router.add_post('/redis', redis_view, name='redis_view')
