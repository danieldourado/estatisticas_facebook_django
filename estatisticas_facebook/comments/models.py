from django.core.urlresolvers import reverse
from django.db import models
from estatisticas_facebook.posts.models import Post
from estatisticas_facebook.users.models import User



class Comment(models.Model):
    id              = models.CharField      (primary_key = True, max_length = 45)
    message         = models.CharField      (max_length = 4500, default="")
    created_time    = models.DateTimeField  (null=True)
    post            = models.ForeignKey     (Post, null=True)
    user            = models.ForeignKey     (User, null=True)
    permalink_url   = models.CharField      (max_length = 450, default="")
    name            = models.CharField      (max_length = 450, default="")

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse('comments:detail', args=[str(self.id)])
