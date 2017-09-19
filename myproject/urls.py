from django.conf.urls import url, include

urlpatterns = [
    # url(r'', include('django.contrib.auth.urls')),
    url(r'', include('apps.crud.urls.defaultUrl')),
    url(r'^admin/', include('apps.crud.urls.urls')),
]