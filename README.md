# 压测对比

## 环境搭建
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt -i https://pypi.douban.com/simple
```

## 1. Flask启动压测

```bash
python demo.py

ab -n 500 -c 500 http://localhost:5000/
```


## 2. Gunicorn启动压测

```bash
# 使用gunicorn启动， 这里启动4个进程
gunicorn -w 4 -b 0.0.0.0:8000 demo:app

ab -n 500 -c 500 http://localhost:8000/
```
