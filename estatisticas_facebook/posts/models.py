from django.db import models
from django.utils.dateformat import DateFormat, TimeFormat
from django.core.urlresolvers import reverse
from estatisticas_facebook.util.graph import getNewGraphApi, debug, get_paged_query
from estatisticas_facebook.pages.models import *
from estatisticas_facebook.comments.models import *
from estatisticas_facebook.reactions.models import *
from estatisticas_facebook.faceusers.models import *

COMMENTS = 'comments'
REACTIONS = 'reactions'
POSTS = 'posts'
FINISHED = 'finished'
QUERY = '/posts?fields=id,name,created_time,story,message,permalink_url,shares.summary(count).as(shares),comments.limit(1),reactions.limit(1),comments.limit(0).summary(total_count).as(total_comments),insights.metric(post_reactions_by_type_total)&pretty=false&limit=100&since='


def save_paging(model, model_name, paging_json):

    if paging_json:
        cursors_next = paging_json.get('cursors').get('after')
    else:
        cursors_next = FINISHED
        
    if model_name == COMMENTS:
        model.comment_paging = cursors_next
    if model_name == REACTIONS:
        model.reaction_paging = cursors_next
    if model_name ==  POSTS:
        model.post_paging = cursors_next
    
    model.save()


def get_item_and_paging(extracting_function, model, model_name, data):

    if data is None:
        return
    
    extracting_function(model, data.get('data'))
    save_paging(model,model_name, data.get('paging'))
    
    
def save_post_data(page_model, data):
    for post in data:
        insights_values = post['insights']['data'][0]['values'][0]['value']
       
        shares = 0    
        if post.get('shares') is not None:
            shares = post['shares']['count']
            
        temp_post = Post(
            page = page_model,
            id = post.get('id'),
            created_time = post.get('created_time'),
            message = post.get('message'),
            permalink_url = post.get('permalink_url'),
            shares = shares,
            total_comments = post['total_comments']['summary']['total_count'],
            post_reactions_like_total = insights_values.get('like'),
            post_reactions_love_total = insights_values.get('love'),
            post_reactions_wow_total = insights_values.get('wow'),
            post_reactions_haha_total = insights_values.get('haha'),
            post_reactions_sorry_total = insights_values.get('sorry'),
            post_reactions_anger_total = insights_values.get('anger'),
            reactions   =insights_values['like']
                        +insights_values['love']
                        +insights_values['wow']
                        +insights_values['haha']
                        +insights_values['sorry']
                        +insights_values['anger'],
            )
        temp_post.save()
        
        get_item_and_paging(save_comment_data, temp_post, COMMENTS, post.get('comments'))
        get_item_and_paging(save_reaction_data, temp_post, REACTIONS, post.get('reactions'))
        
        debug('new post saved: '+temp_post.id)

def get_posts(page_model, since):
    
    paged_query = get_paged_query(page_model.post_paging, QUERY+str(since))
    
    if paged_query:
        data = getNewGraphApi(page_model.id).get_object(page_model.id+paged_query)
    else:
        return

    get_item_and_paging(save_post_data, page_model, POSTS, data)

    get_posts(page_model, since)
     
def getPostInfo(page_model, since):

    Post.objects.filter(page = page_model).delete()
    FaceUsers.objects.all().delete()
    page_model.post_paging = None
    page_model.save()

    get_posts(page_model, since)
    #savePostData(page_model, data)
    
    
class Post(models.Model):
    id                                      = models.CharField(primary_key = True, max_length = 45)
    page                                    = models.ForeignKey('pages.Page', on_delete=models.CASCADE)
    total_comments                          = models.IntegerField(default=0)
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
    created_time                            = models.CharField(max_length = 45, null=True)
    message                                 = models.CharField(max_length = 4500, null=True)
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

