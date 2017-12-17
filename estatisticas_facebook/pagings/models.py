from django.core.urlresolvers import reverse
from django.db import models


class Paging(models.Model):
    model_name  = models.CharField(default="", max_length=64)
    url         = models.CharField(default="", max_length=512)
    name        = models.CharField(max_length = 512, default="")

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse('pagings:detail', args=[str(self.id)])
