from appsetup import appsetup

from django.core.management import call_command

from django.conf.urls import url
from django.http import HttpResponse
from django.db import models

def myview(request):
    return HttpResponse("foo")

urlpatterns = [
    url(r'^$', myview),
]

appsetup(urlpatterns)

if __name__ == "__main__":
    call_command("migrate")
    call_command("runserver", "0.0.0.0:8000")
