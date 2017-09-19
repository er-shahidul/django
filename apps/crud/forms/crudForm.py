from django.forms import ModelForm

from apps.crud.models import Crud


class CrudForm(ModelForm):
    class Meta:
        model = Crud
        fields = ['name', 'ip', 'order']