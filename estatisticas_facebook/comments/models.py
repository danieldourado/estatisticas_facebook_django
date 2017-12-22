from django.core.urlresolvers import reverse
from django.db import models
from estatisticas_facebook.faceusers.models import *

def getComments(post_model, data):

    for comment in data:
        
        user = addInteraction(comment.get('from'), 'comments')
        
        Comment(
            post = post_model,
            id = comment.get('id'),
            created_time = comment.get('created_time'),
            message = comment.get('message'),
            permalink_url = 'https://facebook.com/'+comment.get('id'),
            user = user,
            ).save()
        print('new comment saved: '+comment.get('id'))

class Comment(models.Model):
    id              = models.CharField      (primary_key = True, max_length = 45)
    message         = models.CharField      (max_length = 4500, default="")
    created_time    = models.DateTimeField  (null=True)
    post            = models.ForeignKey     ('posts.Post', null=True, on_delete=models.CASCADE)
    user            = models.ForeignKey     (FaceUsers, null=True)
    permalink_url   = models.CharField      (max_length = 450, default="")
    name            = models.CharField      (max_length = 450, default="")

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse('comments:detail', args=[str(self.id)])
