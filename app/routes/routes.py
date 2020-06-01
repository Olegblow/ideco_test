from views import ServiseView


def setup_routes(app):
    """Создаем маршруты приложения."""
    app.router.add_route('*', '', ServiseView)
