from django.conf.urls import url

from apps.crud.controllers import crudController

urlpatterns = [
    url(r'^crud/list$', crudController.crud_list, name='crud_list'),
    url(r'^crud/new$', crudController.crud_create, name='crud_new'),
    url(r'^crud/edit/(?P<pk>\d+)$', crudController.crud_update, name='crud_edit'),
    url(r'^crud/delete/(?P<pk>\d+)$', crudController.crud_delete, name='crud_delete'),
]
