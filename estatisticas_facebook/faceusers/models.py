from django.core.urlresolvers import reverse
from django.db import models
from util.graph import debug

def getFaceUser(user_json):
    temp_user, created = FaceUsers.objects.get_or_create(id=user_json.get('id'))    
    temp_user.name = user_json.get('name')
    
    return temp_user

def setInteraction(model, interaction):
    interaction = interaction.lower()
    if interaction.lower() in ('like','love','wow','haha','sad','angry', 'pride','thankful'):
        model.reactions += 1
        attribute = 'post_reactions_'+interaction+'_total'
        value = getattr(model, attribute) + 1
        setattr(model, attribute, value)
    else:
        value = getattr(model, interaction) + 1
        setattr(model, interaction, value)
    debug('new user interaction saved: '+interaction)

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
    post_reactions_sad_total                = models.IntegerField(default=0)
    post_reactions_angry_total              = models.IntegerField(default=0)
    post_reactions_pride_total              = models.IntegerField(default=0)
    post_reactions_thankful_total           = models.IntegerField(default=0)
    post_reactions_positivo_total           = models.IntegerField(default=0)
    post_reactions_negativo_total           = models.IntegerField(default=0)
    post_reactions_positivo_porcentagem     = models.IntegerField(default=0)
    post_reactions_negativo_porcentagem     = models.IntegerField(default=0)
    permalink_url                           = models.CharField(max_length = 450, default="")

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse('faceusers:detail', args=[str(self.id)])
