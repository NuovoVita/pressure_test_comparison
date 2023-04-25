from flask import Flask
from flask_redis import FlaskRedis

REDIS_URL = "redis://:Mjolnir@localhost:6379/0"

app = Flask(__name__)
app.config.from_object(__name__)

redis = FlaskRedis(app, True)


@app.route('/')
def index():
    redis.incr('hit', 1)
    return redis.get('hit')


if __name__ == '__main__':
    app.run(thread=True)
