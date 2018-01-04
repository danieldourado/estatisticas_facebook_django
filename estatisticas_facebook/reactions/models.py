from django.core.urlresolvers import reverse
from django.db import models
from estatisticas_facebook.posts.models import *
from estatisticas_facebook.faceusers.models import *
from util.graph_tornado import *


QUERY = '/reactions?limit=100000'


def get_reactions(post):
    
    paged_query = get_paged_query(post.reaction_paging, QUERY)
    
    if paged_query:
        data = getNewGraphApi(post.page.id).get_object(post.id+paged_query)
    else:
        return

    get_item_and_paging(save_reaction_data, post, REACTIONS, data)

    get_reactions(post)
     
def getReactionInfo(page_model):
    
    from estatisticas_facebook.posts.models import Post
    post_list = Post.objects.filter(page = page_model).all()

    i = 0
    for post in post_list:
        if post.reaction_paging is not None and post.reaction_paging != FINISHED:
            i = i+1
            get_reactions(post)
            if i > 70:
                return

def get_user_object_from_reaction_json(reaction):
    user = {}
    user['name'] = reaction.get('name')
    user['id'] = reaction.get('id')
    return user

def save_reaction_data(post_model, data):

    for reaction in data:

        user = addInteraction(get_user_object_from_reaction_json(reaction), reaction.get('type'))
        
        Reaction(
            type = reaction.get('type'),
            user = user,
            post = post_model,
            ).save()
        #debug('new reaction saved: '+reaction.get('type'))


class Reaction(models.Model):
    type                                    = models.CharField(default="", max_length=64)
    user                                    = models.ForeignKey(FaceUsers, null=True)
    post                                    = models.ForeignKey('posts.Post', null=True, on_delete=models.CASCADE)
    name                                    = models.CharField(max_length = 512, default="")

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse('reactions:detail', args=[str(self.id)])
