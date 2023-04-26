import random
import time

from flask import Flask, render_template
from gevent.pywsgi import WSGIServer

app = Flask(__name__)


@app.route('/')
def connect():
    return 'connect successfully'


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    print('Visit hello api')
    time.sleep(random.randint(3, 8))
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    server = WSGIServer(('0.0.0.0', 8000), app)
    print('Server started')
    server.serve_forever()
