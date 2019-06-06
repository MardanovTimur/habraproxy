import aiohttp_debugtoolbar

from aiohttp import web
from aiohttp_debugtoolbar import toolbar_middleware_factory


from app.routes import setup_routes

app = web.Application()
#  aiohttp_debugtoolbar.setup(app)
setup_routes(app)

if __name__ == "__main__":
    web.run_app(app)
