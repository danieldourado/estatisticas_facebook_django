from django.core.urlresolvers import reverse
from django.db import models


class Token(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tokens:detail', args=[str(self.id)])
