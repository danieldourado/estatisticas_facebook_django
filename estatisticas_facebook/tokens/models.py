from django.core.urlresolvers import reverse
from django.db import models
import facebook
import urllib.request, json
from estatisticas_facebook.tokens.models import *


def getLatestSavedToken():
    access_token = Token.objects.filter().order_by('-id')[0]
    return access_token    

def getShortLivedAccessToken(page_name):
    access_token = getLatestSavedToken()
    graph = facebook.GraphAPI(getLatestSavedToken())
    raw_json = graph.get_object(page_name+"?fields=access_token")    
    new_access_token = raw_json['access_token']
    return new_access_token

def makeAccessTokenLongLived(short_lived_access_token):
    url = 'https://graph.facebook.com/oauth/access_token?client_id=571058086572175&client_secret=c3cc91d289a9869e74f6907c9cc68909&grant_type=fb_exchange_token&fb_exchange_token='
    with urllib.request.urlopen(url+short_lived_access_token) as url:
        data = json.loads(url.read().decode())
        return data['access_token']
    
def saveAccessToken(access_token):
    new_token = Token(name=access_token)
    new_token.save()

def getNewAccessToken(page_name):
    access_token = makeAccessTokenLongLived(getShortLivedAccessToken(page_name))
    saveAccessToken(access_token)
    return access_token
    
    
class Token(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tokens:detail', args=[str(self.id)])

