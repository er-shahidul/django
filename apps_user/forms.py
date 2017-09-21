from django.forms import ModelForm

from apps_user.models import User
from apps_user.models.userProfile import Profile


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = 'location',
