from django.core.urlresolvers import reverse
from django.db import models

def getFaceUser(user_json):
    print(user_json)
    temp_user, created = FaceUsers.objects.get_or_create(id=user_json.get('id'))    
    temp_user.name = user_json.get('name')
    
    return temp_user

def setInteraction(model, interaction):
    setattr(model, 'bar', 'BAR')

def addInteraction(user_json, interaction):
    face_user = getFaceUser(user_json)
    
    if interaction is 'like':
        face_user.reactions+=1
        face_user.post_reactions_like_total+=1
        print('new user interaction saved: '+interaction)
    
    face_user.save()
    return face_user
    

class FaceUsers(models.Model):
    id                                      = models.CharField(primary_key = True, max_length = 45)
    name                                    = models.CharField(max_length = 450, default="")
    comments                                = models.IntegerField(default=0)
    shares                                  = models.IntegerField(default=0)
    reactions                               = models.IntegerField(default=0)
    like                                    = models.IntegerField(default=0)
    love                                    = models.IntegerField(default=0)
    wow                                     = models.IntegerField(default=0)
    haha                                    = models.IntegerField(default=0)
    sorry                                   = models.IntegerField(default=0)
    anger                                   = models.IntegerField(default=0)
    post_reactions_positivo_total           = models.IntegerField(default=0)
    post_reactions_negativo_total           = models.IntegerField(default=0)
    post_reactions_positivo_porcentagem     = models.IntegerField(default=0)
    post_reactions_negativo_porcentagem     = models.IntegerField(default=0)
    permalink_url                           = models.CharField(max_length = 450, default="")

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse('faceusers:detail', args=[str(self.id)])
