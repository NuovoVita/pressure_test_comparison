import gevent
import greenlet


def callback(event, args):
    print(event, args[0], '===:>>>>', args[1])


def foo():
    print('Running in foo')
    gevent.sleep(0)
    print('Explicit context switch to foo again')


def bar():
    print('Explicit context to bar')
    gevent.sleep(0)
    print('Implicit context switch back to bar')


print('main greenlet info: {}'.format(greenlet.getcurrent()))
print('hub info {}'.format(gevent.get_hub()))
oldtrace = greenlet.settrace(callback)
gevent.joinall([gevent.spawn(foo), gevent.spawn(bar)])
greenlet.settrace(oldtrace)
