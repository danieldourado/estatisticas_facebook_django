from django.core.urlresolvers import reverse
from django.db import models
from estatisticas_facebook.posts.models import *
from estatisticas_facebook.faceusers.models import *

def get_user_object_from_reaction_json(reaction):
    user = {}
    user['name'] = reaction.get('name')
    user['id'] = reaction.get('id')
    return user

def getReactions(post_model, reaction):
    
    paging = reaction['paging']
    data    = reaction['data']
    
    for reaction in data:
        
        user = addInteraction(get_user_object_from_reaction_json(reaction), reaction.get('type'))
        
        Reaction(
            type = reaction.get('type'),
            user = user,
            post = post_model,
            ).save()
        print('new reaction saved: '+reaction.get('type'))

class Reaction(models.Model):
    type                                    = models.CharField(default="", max_length=64)
    user                                    = models.ForeignKey(FaceUsers, null=True)
    post                                    = models.ForeignKey('posts.Post', null=True, on_delete=models.CASCADE)
    name                                    = models.CharField(max_length = 512, default="")

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse('reactions:detail', args=[str(self.id)])
