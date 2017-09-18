from django.conf.urls import url

from apps.crud.controllers import helpController

urlpatterns = [
    url(r'^help/list$', helpController.help_list, name='help_list'),
    url(r'^help/new$', helpController.help_create, name='help_new'),
    url(r'^help/edit/(?P<pk>\d+)$', helpController.help_update, name='help_edit'),
    url(r'^help/delete/(?P<pk>\d+)$', helpController.help_delete, name='help_delete'),
]
