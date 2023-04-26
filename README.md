# 压测对比

## 环境搭建

Python >= 3.8

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt -i https://pypi.douban.com/simple
```

## 1. Flask 阻塞和非阻塞

```bash
# Flask 压测
python demo.py
ab -n 500 -c 500 http://localhost:5000/

# 1. 纯 Flask 是非阻塞的，可实现并发
python pure_flask_non_blocking.py

# 2. gevent 是阻塞的
python wsgi_flask_blocking.py

# 3. gevent 程序中增加 monkey，实现非阻塞。（备注：monkey将标准socket模块中的函数与类替换为对用的功能项,这样即使不清楚gevent结构,也可从多个greenlet运行环境中受益.）
python wsgi_flask_non_blocking.py


```

## 2. gunicorn启动压测

```bash
# 使用gunicorn启动，这里启动4个进程，gunicorn worker_class default is `-k sync`
gunicorn -w 4 -b 0.0.0.0:8000 demo:app

ab -n 500 -c 500 http://localhost:8000/
wrk -t12 -c400 -d30s --latency http://localhost:8000/
```

## 3. gunicorn 几种 worker 性能测试比较

```bash
gunicorn -w 4 demo:app --worker-class sync
gunicorn -w 4 --thread=2 --worker-class=gthread demo:app # 最大的并发请求就是worker * 线程， 也就是8，在有很多请求时候，线程才会开启
gunicorn -w 4 demo:app --worker-class gevent
gunicorn -w 4 --worker-class=gevent --worker-connections=1000 demo:app # work-connections 是对gevent worker类的特殊设置，最大的并发请求数 是4000（4个worker * 1000连接/worker)
gunicorn -w 4 demo:app --worker-class tornado
gunicorn -w 4 demo:app --worker-class eventlet
```

## 4. Flask 和 Django 的性能

```bash
# 1. flask
python gevent_flask.py
python tornado_flask.py
gunicorn -b 127.0.0.1:8000 pure_flask:app -k sync
gunicorn -b 127.0.0.1:8000 pure_flask:app -k eventlet
gunicorn -b 127.0.0.1:8000 pure_flask:app -k tornado
gunicorn -b 127.0.0.1:8000 pure_flask:app -k gevent

# 2. django
python gevent_django.py
python tornado_django.py
gunicorn -b 127.0.0.1:8000 pure_django:app -k sync
gunicorn -b 127.0.0.1:8000 pure_django:app -k eventlet
gunicorn -b 127.0.0.1:8000 pure_django:app -k tornado
gunicorn -b 127.0.0.1:8000 pure_django:app -k gevent

# 3. tornado
# tornado 从6.0版本不支持其它WSGI服务器上运行了，只能使用自己的服务器
python pure_tornado.py
```

## 5. 建议

1. IO 密集型场景 - 建议使用gevent或者asyncio
2. CPU 密集型场景 - 建议增加workers数量
3. 不确定内存占用? - 建议使用gthread
4. 不知道怎么选择？ - 建议增加workers数量

## 参考

- [秒会的压测工具-wrk](https://zhuanlan.zhihu.com/p/552756287)
- [Gunicorn介绍](https://zhuanlan.zhihu.com/p/102716258)
- [gevent.WSGISERVER](https://zhuanlan.zhihu.com/p/131364462)
- [python-web-test](https://github.com/AngelLiang/python-web-test)
- [Flask框架及阻塞和非阻塞特性](https://blog.csdn.net/Xin_101/article/details/86663627)
