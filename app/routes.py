from app.views import (
    proxy_view,
)

def setup_routes(app):
    app.router.add_route('*', r'/{url:.*}', proxy_view)
