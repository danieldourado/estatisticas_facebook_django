from django.db import models
from django.utils.dateformat import DateFormat, TimeFormat
from django.core.urlresolvers import reverse
from estatisticas_facebook.util.graph import *
from estatisticas_facebook.pages.models import *
from estatisticas_facebook.comments.models import *
from estatisticas_facebook.reactions.models import *
from estatisticas_facebook.faceusers.models import *
import dateutil.parser


#QUERY = '/posts?fields=id,name,created_time,story,message,permalink_url,shares.summary(count).as(shares),comments.limit(1),comments.limit(0).summary(total_count).as(total_comments),insights.metric(post_reactions_by_type_total,post_impressions,post_impressions_unique)&pretty=false&limit=100&since='
QUERY = '/posts?fields=id,name,created_time,story,message,permalink_url,shares.summary(count).as(shares),comments.limit(1),comments.limit(0).summary(total_count).filter(toplevel).as(total_comments_toplevel),comments.limit(0).summary(total_count).filter(stream).as(total_comments_stream),insights.metric(post_reactions_by_type_total,post_impressions,post_impressions_unique)&pretty=false&limit=100&since='

def save_post_data(page_model, data):
    for post in data:
        
        for insight in post['insights']['data']:
            key = insight['name']
            if 'post_reactions_by_type_total' == key:
                post_reactions_by_type_total = insight['values'][0]['value']
            if 'post_impressions' == key:
                post_impressions = insight['values'][0]['value']
            if 'post_impressions_unique' == key:
                post_impressions_unique = insight['values'][0]['value']
       
        shares = 0    
        if post.get('shares') is not None:
            shares = post['shares']['count']
            
        post_reactions_like_total = post_reactions_by_type_total['like']
        post_reactions_love_total = post_reactions_by_type_total['love']
        post_reactions_wow_total = post_reactions_by_type_total['wow']
        post_reactions_haha_total = post_reactions_by_type_total['haha']
        post_reactions_sorry_total = post_reactions_by_type_total['sorry']
        post_reactions_anger_total = post_reactions_by_type_total['anger']
    
        total_reactions=post_reactions_like_total+post_reactions_love_total+post_reactions_wow_total+post_reactions_haha_total+post_reactions_sorry_total+post_reactions_anger_total
            
        total_comments_toplevel = post.get('total_comments_toplevel').get('summary').get('total_count')
        total_comments_stream = post.get('total_comments_stream').get('summary').get('total_count')
        #engajamento_toplevel = total_reactions+shares+total_comments_toplevel
        #engajamento_stream = total_reactions+shares+total_comments_stream
        #taxa_de_engajamento=0
        #if post_impressions != 0:
        #    taxa_de_engajamento = (engajamento/post_impressions)*100
        #post_reactions_positivo_total = post_reactions_like_total+post_reactions_love_total+post_reactions_wow_total+shares
        #post_reactions_negativo_total = post_reactions_anger_total+post_reactions_haha_total+post_reactions_sorry_total+total_comments
        #positivo_mais_negativo = post_reactions_positivo_total+post_reactions_negativo_total
        #post_reactions_positivo_porcentagem=0
        #post_reactions_negativo_porcentagem=0
        #if positivo_mais_negativo != 0:
        #  	post_reactions_positivo_porcentagem = post_reactions_positivo_total/positivo_mais_negativo*100
        #	post_reactions_negativo_porcentagem = post_reactions_negativo_total/positivo_mais_negativo*100
        
        temp_post = Post(
            page = page_model,
            id = post.get('id'),
            created_time = post.get('created_time'),
            message = post.get('message'),
            permalink_url = post.get('permalink_url'),
            shares = shares,
            total_comments_toplevel = total_comments_toplevel,
            total_comments_stream = total_comments_stream,
            post_reactions_like_total = post_reactions_like_total,
            post_reactions_love_total = post_reactions_love_total,
            post_reactions_wow_total = post_reactions_wow_total,
            post_reactions_haha_total = post_reactions_haha_total,
            post_reactions_sorry_total = post_reactions_sorry_total,
            post_reactions_anger_total = post_reactions_anger_total,
        #    post_reactions_positivo_total=post_reactions_positivo_total,
        #    post_reactions_negativo_total=post_reactions_negativo_total,
        #    post_reactions_positivo_porcentagem=post_reactions_positivo_porcentagem,
        #    post_reactions_negativo_porcentagem=post_reactions_negativo_porcentagem,
            reactions = total_reactions,
            post_impressions=post_impressions,
            post_impressions_unique=post_impressions_unique,
        #    engajamento=engajamento,
        #    taxa_de_engajamento=taxa_de_engajamento,
            )
        temp_post.save()
        
        get_item_and_paging(save_comment_data, temp_post, COMMENTS, post.get('comments'))
        get_item_and_paging(save_reaction_data, temp_post, REACTIONS, post.get('reactions'))
        


def get_posts(page_model, since):
    
    paged_query = get_paged_query(page_model.post_paging, QUERY+str(since))
    
    if paged_query:
        data = get_graph_object(page_model.id,page_model.id+paged_query)
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
    since = dateutil.parser.parse(since+' 01:00:00-00')
    page_model.post_since = since
    page_model.save()
    #savePostData(page_model, data)
    
    
class Post(models.Model):
    id                                      = models.CharField(primary_key = True, max_length = 45)
    page                                    = models.ForeignKey('pages.Page', on_delete=models.CASCADE)
    total_comments_stream                   = models.IntegerField(default=0)
    total_comments_toplevel                 = models.IntegerField(default=0)
    shares                                  = models.IntegerField(default=0)
    reactions                               = models.IntegerField(default=0)
    post_reactions_like_total               = models.IntegerField(default=0)
    post_reactions_love_total               = models.IntegerField(default=0)
    post_reactions_wow_total                = models.IntegerField(default=0)
    post_reactions_haha_total               = models.IntegerField(default=0)
    post_reactions_sorry_total              = models.IntegerField(default=0)
    post_reactions_anger_total              = models.IntegerField(default=0)
    #post_reactions_positivo_total           = models.IntegerField(default=0)
    #post_reactions_negativo_total           = models.IntegerField(default=0)
    #post_reactions_positivo_porcentagem     = models.FloatField(default=0)
    #post_reactions_negativo_porcentagem     = models.FloatField(default=0)
    post_impressions                        = models.IntegerField(default=0)
    post_impressions_unique                 = models.IntegerField(default=0)
    #engajamento_toplevel                    = models.IntegerField(default=0)
    #engajamento_stream                      = models.IntegerField(default=0)
    #taxa_de_engajamento                     = models.FloatField(default=0)
    created_time                            = models.CharField(max_length = 45, null=True)
    message                                 = models.CharField(max_length = 18000, null=True)
    permalink_url                           = models.CharField(max_length = 450, null=True)
    name                                    = models.CharField(max_length = 450, default="")
    reaction_paging                         = models.CharField(max_length = 512, null=True)
    comment_paging                          = models.CharField(max_length = 512, null=True)
    created                                 = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.id

    @property
    def title(self):
        return self.id

    def get_absolute_url(self):
        return reverse('posts:detail', args=[str(self.id)])

