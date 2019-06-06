from aiohttp import (
    web,
    ClientSession,
    request as aiorequest,
)

from app.lib import handle_response

PROXY_URL = 'http://habr.com'


async def proxy_view(request):
    async with ClientSession() as session:
        async with session.get(f'{PROXY_URL}{request.raw_path}') as resp:
            headers = dict(resp.headers)
            headers.pop('Content-Encoding', None)
            headers.pop('Transfer-Encoding', None)
            content_type = headers.get('Content-Type', 'text/plain')
            if 'image' in content_type or '.svg' in request.raw_path:
                return web.Response(body=await resp.read(), content_type=content_type)

            text = await resp.text()

            text = await handle_response(text)

            return web.Response(body=text.encode('utf-8', 'ignore'),
                                status=resp.status,
                                headers=headers)
    return web.Response(text='Oups smth went wrong!')
