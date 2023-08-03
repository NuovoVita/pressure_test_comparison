import logging

logging.basicConfig(
    format='[%(asctime)s] [%(process)d] [%(levelname)s] [%(pathname)s:%(lineno)d]: %(message)s',
    level=logging.DEBUG
)


class BaseCls(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __getattribute__(self, attr):
        logging.debug("__getattribute__ is called")
        try:
            return super().__getattribute__(attr)
        except AttributeError:
            logging.debug(f'have no attr of {attr}')


def test_base_cls():
    a = BaseCls('jyz', 200)
    logging.info(a.name)
    logging.info(a.age)
    logging.info(a.gender)


if __name__ == '__main__':
    test_base_cls()
