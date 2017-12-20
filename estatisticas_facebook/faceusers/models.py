from django.core.urlresolvers import reverse
from django.db import models

def getFaceUser(user_json):
    print(user_json)
    temp_user, created = FaceUsers.objects.get_or_create(id=user_json.get('id'))    
    temp_user.name = user_json.get('name')
    
    return temp_user

def setInteraction(model, interaction):
    value = getattr(model, interaction) + 1
    setattr(model, interaction, value)
    
    if interaction is 'like' or 'love' or 'wow' or 'haha' or 'sorry' or 'anger':
        model.reactions += 1
    
    print('new user interaction saved: '+interaction)

def addInteraction(user_json, interaction):
    face_user = getFaceUser(user_json)
    setInteraction(face_user, interaction)

    face_user.save()
    return face_user
    

class FaceUsers(models.Model):
    id                                      = models.CharField(primary_key = True, max_length = 45)
    name                                    = models.CharField(max_length = 450, default="")
    comments                                = models.IntegerField(default=0)
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
    permalink_url                           = models.CharField(max_length = 450, default="")

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse('faceusers:detail', args=[str(self.id)])
