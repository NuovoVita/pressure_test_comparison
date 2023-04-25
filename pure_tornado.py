import os.path
from abc import ABC

import tornado.ioloop
import tornado.web
import tornado.wsgi


class MainHandler(tornado.web.RequestHandler, ABC):
    def get(self):
        self.write("Hello World!")


class JsonHandler(tornado.web.RequestHandler, ABC):
    def get(self):
        self.finish({'message': 'ok'})


class TemplateHandler(tornado.web.RequestHandler, ABC):
    def get(self):
        self.render('main_for_tornado.html', number=5, messages="whatever", title="home")


settings = {
    "static_path": os.path.join(os.path.dirname(__file__), 'static'),
    "template_path": "templates",
}


def make_app():
    return tornado.web.Application(
        [
            (r"/", MainHandler),
            (r"/template", TemplateHandler),
            (r"/json", JsonHandler),
        ],
        **settings
    )


if __name__ == '__main__':
    app = make_app()
    app.listen(8000, '0.0.0.0')
    tornado.ioloop.IOLoop.current().start()
