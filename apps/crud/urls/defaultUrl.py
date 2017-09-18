from django.conf.urls import url

from apps.crud.controllers import defaultController

urlpatterns = [
    url(r'^$', defaultController.home, name='home'),
    url(r'^homepage/$', defaultController.home, name='home'),
]
