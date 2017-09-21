from django.conf.urls import url

from apps_user.controller import update_profile

urlpatterns = [
    url(r'^add$', update_profile, name='update_profile'),
]
