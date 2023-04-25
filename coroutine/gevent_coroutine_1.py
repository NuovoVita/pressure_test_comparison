import gevent


def func1():
    for i in range(5):
        print('run func1: index = {}'.format(i))
        gevent.sleep(0)


def func2():
    for i in range(5):
        print('run func2: index = {}'.format(i))
        gevent.sleep(0)


t1 = gevent.spawn(func1)
t2 = gevent.spawn(func2)
gevent.joinall([t1, t2])
