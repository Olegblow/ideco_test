from .views import index


# add_routes add_get add_post add_static add_view etc...


def setup_routes(app):
    """Создаем маршруты приложения."""
    app.router.add_get('', index, name='index')
