from bottle import request, response
from bottle import post, get, put, delete
import json

options = []


@post('/set')
def set_options():
    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
    try:
        # parse input data
        try:
            data = request.json()
        except:
            raise ValueError

        if data is None:
            raise ValueError

        options = data.options
        print(options)
        return json.dumps({'result': 'ok'})

    except ValueError:
        response.status = 400
        return


@get('/step/<current>/<next>')
def step(current, next):
    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
    return json.dumps({'result': 'ok', 'guess': '123456789'})
