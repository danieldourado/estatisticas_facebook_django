from django.core.urlresolvers import reverse
from django.db import models


class FaceUsers(models.Model):
    id                                      = models.CharField(primary_key = True, max_length = 45)
    comments                                = models.IntegerField(default=0)
    shares                                  = models.IntegerField(default=0)
    reactions                               = models.IntegerField(default=0)
    post_reactions_like_total               = models.IntegerField(default=0)
    post_reactions_love_total               = models.IntegerField(default=0)
    post_reactions_wow_total                = models.IntegerField(default=0)
    post_reactions_haha_total               = models.IntegerField(default=0)
    post_reactions_sorry_total              = models.IntegerField(default=0)
    post_reactions_anger_total              = models.IntegerField(default=0)
    post_reactions_positivo_total           = models.IntegerField(default=0)
    post_reactions_negativo_total           = models.IntegerField(default=0)
    post_reactions_positivo_porcentagem     = models.IntegerField(default=0)
    post_reactions_negativo_porcentagem     = models.IntegerField(default=0)
    permalink_url                           = models.CharField(max_length = 450, default="")
    name                                    = models.CharField(max_length = 450, default="")

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse('faceusers:detail', args=[str(self.id)])
