from django.core.urlresolvers import reverse
from django.db import models
from estatisticas_facebook.posts.models import Post
from estatisticas_facebook.faceusers.models import FaceUsers


class Reaction(models.Model):
    id                                      = models.CharField(primary_key = True, max_length = 45)
    type                                    = models.CharField(default="", max_length=64)
    user                                    = models.ForeignKey(FaceUsers, null=True)
    post                                    = models.ForeignKey(Post, null=True)
    name                                    = models.CharField(max_length = 512, default="")

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse('reactions:detail', args=[str(self.id)])
