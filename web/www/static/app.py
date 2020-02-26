import logging
logging.basicConfig(level=logging.INFO)
from aiohttp import web
'''async def index(request):
    return web.Response(text="hello world")

app=web.Application()
app.add_routes([web.get('/',index)])
logging.info('server start at port 8080')
web.run_app(app)'''

routes = web.RouteTableDef()


@routes.get('/')
def index(request):
    return web.Response(body=b'<h1>Awesome App</h1>', content_type='text/html')


def init():
    app = web.Application()
    app.add_routes(routes)
    logging.info('server started')
    web.run_app(app)


init()