from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from django.utils.dateformat import DateFormat, TimeFormat


# Create your models here.
class Page(models.Model):
    name            = models.CharField(max_length = 4000)
    pretty_name     = models.CharField(max_length = 4000,null=True, blank=True)
    paging_next     = models.CharField(max_length = 4000,null=True, blank=True)
    access_token    = models.CharField(max_length = 4500,null=True, blank=True)
    since           = models.DateField()
    created         = models.DateTimeField(auto_now_add=True)
    slug            = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def title(self):
        return self.name

class PageInsights(models.Model):
    page            = models.ForeignKey(Page)
    value           = models.IntegerField()
    end_time        = models.DateTimeField()
    period          = models.CharField(max_length = 50)
    title           = models.CharField(max_length = 4500)
    description     = models.CharField(max_length = 4500)
    name            = models.CharField(max_length = 4500)
    created         = models.DateTimeField(auto_now_add=True)
    slug            = models.SlugField(null=True, blank=True)
    
    def __str__(self):
        return str(DateFormat(self.end_time).format('Y-m-d'))    +': '+ self.title+' '+str(self.value)


def rl_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


#def rl_post_save_reciever(sender, instance, *args, **kwargs):



pre_save.connect(rl_pre_save_reciever, sender=PageInsights)
pre_save.connect(rl_pre_save_reciever, sender=Page)

#post_save.connect(rl_pre_save_reciever, sender=PageInsights)

