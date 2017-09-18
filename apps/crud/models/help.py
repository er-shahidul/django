from django.db import models
from django.core.urlresolvers import reverse


class Help(models.Model):
    name = models.CharField(max_length=200)
    order = models.IntegerField()

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('help_edit', kwargs={'pk': self.pk})
