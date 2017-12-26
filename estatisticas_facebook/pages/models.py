from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from django.utils.dateformat import DateFormat, TimeFormat
from util.graph import * 

def getPageInfo(page):
    raw_json = getNewGraphApi(page.name).get_object(page.name)
    print (raw_json)
    page.pretty_name = raw_json['name']
    page.id = raw_json['id']

def getPageInsights(args):

    since = args['since']
    raw_json = getNewGraphApi(args['id']).get_object(args['id']+'/insights?period=day&metric=page_fan_adds_unique,page_impressions_unique,page_engaged_users,page_stories,page_storytellers&since='+str(since))
    
    pagedata = raw_json['data']

    for obj in pagedata:
        print (obj['name'])
        for value in obj['values']:
            page_insights = PageInsights(
                name=obj['name'], 
                period=obj['period'], 
                title=obj['title'], 
                description=obj['description'], 
                end_time=value['end_time'], 
                value=value['value'], 
                page_id=args['id'])
            page_insights.save()


# Create your models here.
class Page(models.Model):
    id              = models.CharField(primary_key = True, max_length = 45)
    name            = models.CharField(max_length = 4000, unique=True)
    pretty_name     = models.CharField(max_length = 4000,null=True, blank=True)
    access_token    = models.CharField(max_length = 4500,null=True, blank=True)
    created         = models.DateTimeField(auto_now_add=True)
    slug            = models.SlugField(null=True, blank=True)
    post_paging     = models.CharField(max_length = 512, null=True)

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

def page_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.pretty_name:
        getPageInfo(instance)
        
def slug_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        
#def rl_post_save_reciever(sender, instance, *args, **kwargs):



pre_save.connect(slug_pre_save_reciever, sender=PageInsights)
pre_save.connect(slug_pre_save_reciever, sender=Page)
pre_save.connect(page_pre_save_reciever, sender=Page)

#post_save.connect(rl_pre_save_reciever, sender=PageInsights)

