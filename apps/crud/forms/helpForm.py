from django.forms import ModelForm

from apps.crud.models import Help


class HelpForm(ModelForm):
    class Meta:
        model = Help
        fields = ['name', 'order']