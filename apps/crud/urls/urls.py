from django.conf.urls import url, include

urlpatterns = [
    url(r'', include('apps.crud.urls.defaultUrl')),
    url(r'', include('apps.crud.urls.crudUrl')),
    url(r'', include('apps.crud.urls.helpUrl')),
]