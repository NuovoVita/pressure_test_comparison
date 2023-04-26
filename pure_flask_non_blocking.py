import random
import time

from flask import Flask, render_template

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
    app.run(host='0.0.0.0', port=8000, debug=True)
