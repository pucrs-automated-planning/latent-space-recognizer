import bottle
import json
import api

app = application = bottle.default_app()


def run():
    bottle.run(host='127.0.0.1', port=8000)
