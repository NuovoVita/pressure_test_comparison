from greenlet import greenlet, getcurrent


def test1(x, y):
    print(id(getcurrent()), id(getcurrent().parent))
    z = gr2.switch(x + y)
    print('back z', z)


def test2(u):
    print(id(getcurrent()), id(getcurrent().parent))
    print('test2 ', u)
    print('B')
    return 'hehe'


gr1 = greenlet(test1)
gr2 = greenlet(test2)
print(id(getcurrent()), id(gr1), id(gr2))
# print(gr1.switch("hello", " world"))
print(gr1.switch("hello", " world"), 'back to main')
