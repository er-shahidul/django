from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'', include(admin.site.urls)),
    url(r'', include('apps.crud.urls.crudUrl')),
    url(r'', include('apps.crud.urls.helpUrl')),
]