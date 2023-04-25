import base64
import json
import sys
import time
from pathlib import Path

from django.conf import settings
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path

settings.configure(
    DEBUG=True,
    SECRET_KEY=base64.b64encode(str(time.time()).encode()),
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
    TEMPLATES=[
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [Path(__file__).resolve().parent.joinpath('templates')],
            'APP_DIRS': True,
        }
    ]
)


def index(request):
    return HttpResponse('Hello World!')


def template_handle(request):
    return render(request, 'main_for_django.html', {'messages': "whatever", 'title': "home", 'range': range(1000)})


def json_handle(request):
    resp = {'statue': 1, 'message': 'OK', "data": {}}
    return HttpResponse(json.dumps(resp), content_type="application/json")


urlpatterns = (
    path("", index),
    path("template", template_handle),
    path("json", json_handle)
)

app = get_wsgi_application()

if __name__ == '__main__':
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
