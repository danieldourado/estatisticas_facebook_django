from django.core.urlresolvers import reverse
from django.db import models
from estatisticas_facebook.faceusers.models import *
from util.graph import *

QUERY = '/comments?limit=100000'


def get_comments(post):
    
    paged_query = get_paged_query(post.comment_paging, QUERY)
    
    if paged_query:
        data = getNewGraphApi(post.page.id).get_object(post.id+paged_query)
    else:
        return

    get_item_and_paging(save_comment_data, post, COMMENTS, data)

    get_comments(post)
     
def getCommentInfo(page_model):
    
    from estatisticas_facebook.posts.models import Post
    post_list = Post.objects.filter(page = page_model).all()

    for post in post_list:
        if post.comment_paging is not None and post.comment_paging != FINISHED:
            get_comments(post)



def save_comment_data(post_model, data):

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
        debug('new comment saved: '+comment.get('id'))

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
