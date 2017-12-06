from django.db import models
from pages.models import Page
from django.utils.dateformat import DateFormat, TimeFormat
from django.core.urlresolvers import reverse


class Post(models.Model):
    id                              = models.CharField(primary_key = True, max_length = 45)
    page                            = models.ForeignKey(Page)
    comments                        = models.IntegerField()
    shares                          = models.IntegerField()
    reactions                       = models.IntegerField()
    post_reactions_like_total       = models.IntegerField()
    post_reactions_love_total       = models.IntegerField()
    post_reactions_wow_total        = models.IntegerField()
    post_reactions_haha_total       = models.IntegerField()
    post_reactions_sorry_total      = models.IntegerField()
    post_reactions_anger_total      = models.IntegerField()
    post_reactions_positivo_total   = models.IntegerField()
    post_reactions_negativo_total   = models.IntegerField()
    created_time                    = models.CharField(max_length = 45)
    message                         = models.CharField(max_length = 4500)
    permalink_url                   = models.CharField(max_length = 4500)
    created                         = models.DateTimeField(auto_now_add=True)
    name                            = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.id

    @property
    def title(self):
        return self.id

    def get_absolute_url(self):
        return reverse('posts:detail', args=[str(self.id)])

