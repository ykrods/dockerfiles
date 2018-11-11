import sys

from types import ModuleType

from django import setup
from django.apps import AppConfig
from django.conf import settings
from django.conf import global_settings
from django.core.management import call_command

configure_default = {
    'DEBUG': True,
    'DATABASES': {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": ":memory:",
        },
    },
    'INSTALLED_APPS': global_settings.INSTALLED_APPS,
    'ROOT_URLCONF': 'urls',
    'ALLOWED_HOSTS': ['localhost'],
}

def appsetup(urlpatterns, configure={}):
    urls = ModuleType('urls')
    urls.urlpatterns = urlpatterns

    sys.modules['urls'] = urls

    c = dict(configure_default, **configure)
    # c["INSTALLED_APPS"].append(appname)
    settings.configure(**c)

    setup()
