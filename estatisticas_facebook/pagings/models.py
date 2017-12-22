from django.core.urlresolvers import reverse
from django.db import models

def save_paging(post_model, model_name, paging_json):
    Paging(
            model_name      = model_name,
            cursor_after    = paging_json.get('cursors').get('before'),
            cursor_before   = paging_json.get('cursors').get('after'),
            post            = post_model,
            
        ).save()

class Paging(models.Model):
    model_name      = models.CharField(default="", max_length=64)
    cursor_after    = models.CharField(default="", max_length=512)
    cursor_before   = models.CharField(default="", max_length=512)
    post            = models.ForeignKey('posts.Post', null=True, on_delete=models.CASCADE)
    name            = models.CharField(max_length = 512, default="")
    

    def __str__(self):
        return self.model_name

    def get_absolute_url(self):
        return reverse('pagings:detail', args=[str(self.id)])
