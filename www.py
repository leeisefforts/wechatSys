from application import app

from web.controller.index import route_api

app.register_blueprint(route_api, url_prefix='/api')
