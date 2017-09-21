from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps_user.repository import UserRepository


class User(AbstractUser):
    """User model."""

    username = models.CharField(max_length=30, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    # avatar = models.ImageField('profile picture', upload_to='static/avatars/', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserRepository()

    # def set_avatar(self):
    #     _avatar = self.avatar
    #     if not _avatar:
    #         self.avatar = "static/avatars/avatar.png"