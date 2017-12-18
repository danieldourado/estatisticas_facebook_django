from django.db import models
from pages.models import Page
from django.utils.dateformat import DateFormat, TimeFormat
from django.core.urlresolvers import reverse
from util.graph import *

def getPostInfo(page_id):
    postsQuery = '/posts?fields=id,name,created_time,story,message,permalink_url,shares,comments.limit(1),reactions.limit(1),comments.limit(0).summary(total_count).as(total_comments),insights.metric(post_reactions_by_type_total)'
    raw_json = getNewGraphApi(page_id).get_object(page_id+postsQuery)
    print(raw_json)
    
class Post(models.Model):
    id                                      = models.CharField(primary_key = True, max_length = 45)
    page                                    = models.ForeignKey(Page)
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
    created_time                            = models.CharField(max_length = 45)
    message                                 = models.CharField(max_length = 4500)
    permalink_url                           = models.CharField(max_length = 450, default="")
    created                                 = models.DateTimeField(auto_now_add=True)
    name                                    = models.CharField(max_length = 450, default="")
    reaction_paging                         = models.CharField(max_length = 512, null=True)
    comment_paging                          = models.CharField(max_length = 512, null=True)
    
    def __str__(self):
        return self.id

    @property
    def title(self):
        return self.id

    def get_absolute_url(self):
        return reverse('posts:detail', args=[str(self.id)])

