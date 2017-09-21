from django.conf.urls import url, include

urlpatterns = [
    # url(r'', include('django.contrib.auth.urls')),
    url(r'', include('apps.crud.urls.defaultUrl')),
    url(r'^user/', include('apps_user.userUrl')),
    url(r'^admin/', include('apps.crud.urls.urls')),
]