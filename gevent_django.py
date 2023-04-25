from gevent.pywsgi import WSGIServer

from pure_django import app

http_server = WSGIServer(('', 8000), app)
http_server.serve_forever()
